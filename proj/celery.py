import traceback
from celery import shared_task
import os
from time import sleep
from typing import Any, List, Tuple, Union
from proj.settings import CELERY_BROKER_URL
from celery import Celery, bootsteps
from kombu.message import Message
import kombu
import logging
logger = logging.getLogger('proj')
logger.info(f'{CELERY_BROKER_URL=}')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

test_routing_key = 'test'
test_queue_name = 'test_queue'

routes: List[Tuple[str, str]] = [
    (test_queue_name, test_routing_key),
]

exchange_name = 'some_exchange'


def get_testing_task(app: Celery):
  @shared_task
  def testing_task(message: dict) -> None:
    with app.producer_pool.acquire(block=True) as producer:
      producer.publish(
          message,
          exchange=exchange_name,
          delivery_mode=2,
          routing_key=test_routing_key,
      )
  return testing_task


testing_task = get_testing_task(app)


def build_queues(APP: Celery, pre_routes: Union[List[Tuple[str, str]], None] = None):
  itereable = pre_routes if pre_routes is not None else routes
  with APP.pool.acquire(block=True) as conn:
    exchange = kombu.Exchange(
        name=exchange_name,
        type='direct',
        durable=True,
        channel=conn,
    )
    exchange.declare()
    queues: List[kombu.Queue] = []
    for queue_name, routing_key in itereable:
      hour = 60 * 60
      ttl_time = hour * 24 * 5  # 5 days

      queue = kombu.Queue(
          queue_name,
          kombu.Exchange(exchange_name),
          routing_key=routing_key,
          channel=conn,
          message_ttl=ttl_time,
          queue_arguments={
              'x-queue-type': 'classic',
              'x-message-ttl': ttl_time,
              'x-dead-letter-exchange': 'default',
              'x-expires': ttl_time,
          },
          durable=True)
      queue.declare()
      queues.append(queue)
    return queues


class CrawlerConsumerStep(bootsteps.ConsumerStep):

  def get_consumers(self, channel: Any) -> Any:
    return [kombu.Consumer(channel,
                           queues=build_queues(app, routes),
                           callbacks=[self.handle_message],
                           accept=['json'])]

  def handle_message(self, params: dict, message: Message) -> None:

    message_routing_key: str = message.delivery_info['routing_key']
    logger.info(f'{message=}\n{message_routing_key=}\n{params=}')
    try:
      sleep(params.get('wait', 300))

      message.ack()
    except Exception as e:
      trcb = traceback.format_exc()
      logger.error(f"Error while handling Rabbit task: {e} \n {trcb}")
      raise ValueError('A very specific bad thing happened.')


app.steps['consumer'].add(CrawlerConsumerStep)

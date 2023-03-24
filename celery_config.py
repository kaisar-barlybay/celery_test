
import environ  # type: ignore
env = environ.Env()
environ.Env.read_env()

# CELERY
RABBITMQ_USER = env('RABBITMQ_USER', default='guest')
RABBITMQ_PASSWORD = env('RABBITMQ_PASSWORD', default='guest')
RABBITMQ_HOST = env('RABBITMQ_HOST', default='127.0.0.1:5672')

# CELERY_BROKER_HEARTBEAT = 10
# CELERY_BROKER_CONNECTION_TIMEOUT = 30
# CELERY_WORKER_CONCURRENCY = 50
# CELERY_TASK_ACKS_LATE = True

# CELERY_WORKER_SEND_TASK_EVENT=False
# CELERY_TASK_ACKS_LATE=False
# CELERY_WORKER_PREFETCH_MULTIPLIER = 10
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

# CELERY_BROKER_POOL_LIMIT = 1 # Will decrease connection usage
# CELERY_RESULT_BACKEND = None # AMQP is not recommended as result backend as it creates thousands of queues
# CELERY_EVENT_QUEUE_EXPIRES = 60 # Will delete all celeryev. queues without consumers after 1 minute.
# CELERY_WORKER_PREFETCH_MULTIPLIER = 1 # Disable prefetching, it's causes problems and doesn't help performance

broker_url = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/"
task_acks_late = True
worker_prefetch_multiplier = 1
celeryd_concurrency=1
concurrency=1
heartbeat = 60
broker_heartbeat = 60
# broker_heartbeat = 3600
# heartbeat = 3600
# worker_send_task_event = False
# task_ignore_result = True
# task will be killed after 60 seconds
# task_time_limit = 3600
# task will raise exception SoftTimeLimitExceeded after 50 seconds
# task_soft_time_limit = 3600
# task messages will be acknowledged after the task has been executed, not just before (the default behavior).
# task_acks_late = True
# One worker taks 10 tasks from queue at a time and will increase the performance
# worker_prefetch_multiplier = 1
# worker_concurrency=1
# broker_pull_limit=1
from proj.celery import testing_task


if __name__ == '__main__':
  for i in range(10000):
    testing_task({'wait': 360})

## Test case

1. run rabbitmq locally: `docker-compose up -d`
2. create virtual env: `python -m venv env`
3. activate environment: `env\Scripts\activate`
4. install requirements: `pip install -r requrements.txt`
5. check that app works: `python manage.py runserver`
6. run celery instance locally (it will create test_queue and test_exchange): `celery -A proj.celery worker -l debug -c 1 -n worker_celery_test --without-heartbeat --without-gossip --without-mingle`
7. publish test messages: `python producer.py`
8. run pods locally in kubernetes (kind in my case) `kubectl apply -f celery_test.yaml`

## Other commands (build & push image to dockerhub)

```
docker build -t kaisar7barlybay/celery_test:latest .
docker push kaisar7barlybay/celery_test:latest
```

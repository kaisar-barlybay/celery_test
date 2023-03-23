## test-case

1. run rabbitmq locally: `docker-compose up -d`
2. run pods in kubernetes (kind in my case) `kubectl apply -f celery_test.yaml`

## debug app locally

1. install requirements: `pip install -r requrements.txt`
2. check that app works: `python manage.py runserver`
3. run celery instance locally: `celery -A proj.celery worker -l info -c 1 -n worker_celery_test`

## build & push image to dockerhub

```
docker build -t <myrepo.git>:<mytag> .
docker push <myrepo.git>:<mytag>
```

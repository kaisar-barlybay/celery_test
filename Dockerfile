FROM python:3.8
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip

# essentials
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /var/log/celery -p
RUN touch /var/log/celery/celery.log

COPY . .
EXPOSE 8080
CMD celery -A proj.celery worker -l info -c 1 -n worker_celery_test
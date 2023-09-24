FROM python:3.11

WORKDIR /picasso

RUN apt update && apt install -y postgresql-client
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY . .
RUN pip install -r requirements.txt

RUN chmod +x ./wait-for-postgres.sh
RUN chmod +x ./django-entrypoint.sh
RUN chmod +x ./celery-entrypoint.sh

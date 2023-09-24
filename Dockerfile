FROM python:3.11-alpine

WORKDIR /picasso

RUN apk update && apk add postgresql-client
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY . .
RUN pip install -r requirements.txt

RUN chmod +x ./wait-for-postgres.sh

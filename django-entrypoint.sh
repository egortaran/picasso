#!/bin/sh

./wait-for-postgres.sh

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn picasso.wsgi --bind 0.0.0.0:8000

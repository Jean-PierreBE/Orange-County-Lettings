#!/bin/bash 

#comment
set -e 

source /env/bin/activate 
python manage.py makemigrations 
python manage.py migrate
python manage.py collectstatic --noinput

exec python manage.py runserver 0.0.0.0:8000
#!/bin/sh

echo "Rolling migrations"
python manage.py migrate

echo "Creating mock data"
python manage.py loaddata fixtures/assemblies.json
python manage.py loaddata fixtures/baseProducts.json

echo "Running server"
python manage.py runserver 0.0.0.0:8000

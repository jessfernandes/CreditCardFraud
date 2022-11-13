#!/bin/bash

echo "-----> Making migrations"
python manage.py makemigrations

echo "-----> Migrating"
python manage.py migrate

echo "-----> Creating super user"
python manage.py shell < ./scripts/create_users.py    

echo "-----> Starting server"
python manage.py runserver 0.0.0.0:$APPLICATION_PORT

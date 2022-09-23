#!/bin/bash

source env/bin/activate

source /usr/share/nginx/html/test_ci_cd

python3 manage.py makemigrations
python3 manage.py migrate 

echo "Migrations done"


sudo cp -rf gunicorn.socket /etc/systemd/system/
sudo cp -rf gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"

sudo service daemon-reload
sudo service gunicorn start
sudo service gunicorn enable

echo "Gunicorn has been started"

sudo service gunicorn status
sudo service gunicorn restart 
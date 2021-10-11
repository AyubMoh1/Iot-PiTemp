#!/bin/bash

ssh pi@192.168.1.11 /home/pi/temperatureguage/bootclient.sh &

cd server

pipenv install

pipenv run python tempserver.py &

cd -

cd flask-example

pipenv install


export FLASK_APP=vizualisr

pipenv run flask run


echo "done!"

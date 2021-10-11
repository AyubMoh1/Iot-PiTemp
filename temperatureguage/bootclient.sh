#!/bin/bash
cd /home/pi/temperatureguage

pipenv install


pipenv run python tempclient.py


echo "done!"

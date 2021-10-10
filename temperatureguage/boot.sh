#!/bin/bash

pipenv install


wait


pipenv run python tempclient.py


echo "done!"


# Iot-PiTemp


## Table of contents


* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)




## General info

This project aim is to create a simple IoT device for sending and reciving temperature data over mqtt. 


## Tehnologies

Project is created with :
*Headless Raspberry pi zero WH running Raspberry Pi OS Lite(32bit).
*Ds18b20 temperature sensor.
*Mqtt broker and server.


## Setup

To run this project you need to move 'temperatureguage' to the rpi this directory should contain 'tempguage.py', 'tempclient.py', 'Pipfile' and 'bootclient.sh'. The 'bootclient.sh' which is a script that starts pipenviroment and client is optional.

** 'tempclient.py' line 14 must match the brokers IP(the machine that runs 'tempserver.py'.  **

to start the server:
```
 $cd server
 $pipenv install
 $pipenv shell
 $python tempserver.py
```
to start the client:
 ```
 $./bootclient.sh
 ```
--------or------------
 ```
 $pipenv install 
 $pipenv shell
 $python tempclient.py
```
to start flask:
```
$pipenv install
$ $Env:FLASK_APP="vizualisr"
$ pipenv shell
$ flask run
```

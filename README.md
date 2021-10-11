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
*4,7kΩ resistor


## Setup

To run this project you need to move 'temperatureguage' to the rpi this directory should contain 'temperatureguage.py', 'temperatureclient.py', 'Pipfile' and 'bootclient.sh'. The 'bootclient.sh' which is a script that starts pipenviroment and client is optional.

** 'tempclient.py' line 14 must match the brokers IP(the machine that runs 'tempserver.py'.  **


to start using the boot script type ./boot.sh

--------------or----------

to start the server:
from server folder
```
 $ cd server
 $ pipenv install
 $ pipenv shell
 $ python temperatureserver.py
```
to start the client:
 from temperatureguage folder
 ```
 $ pipenv install 
 $ pipenv shell
 $ python temperatureclient.py
 ```
to start flask:
 from flask-exempel folder
```
$ pipenv install
$ $Env:FLASK_APP="vizualisr"
$ pipenv shell
$ flask run
```

circuit diagram

![image](https://user-images.githubusercontent.com/89800658/136815718-bf1b7a85-c532-4a3b-a7b9-89e12cd1725a.png)

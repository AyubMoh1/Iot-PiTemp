from flask import Flask, render_template, flash
import datetime
import sys
import os
import csv

txtPath = "c:/Users/aom/Desktop/Iot-PiTemp-main/flask-example/vizualisr/temperature.txt"
# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)
# The mapping of units in accordance with our specification
UNITS = {
    0: "°C",
    1: "RH"
}

def read_and_split_string():
    with open("temperature.txt","r") as file:
        string = file.readline()
        list = string.split()
        return list
    
def test_ID(ID_string):
    if ID_string not in list_of_sensors:
        list_of_sensors.append(ID_string)

with open(txtPath, "r") as file:
        #file.write(f"{var1}\n")   
    for line in file:
        print(line, end="")


# This is a placeholder that returns a fixed set of meters
# in a proper system this would look in a database or in
# the file system for a list of meters in the system
def get_meters():
    meters = [ ("id_1", 0),
               ("1234", 1),
               ("1235", 0),
               ("1236", 0)]
    return meters

# This is a placeholder that returns a fixed set of 
# measurement data. In a proper system this would read
# the data from a database or the file system
def get_measurements(meter, channel):
    if (meter, int(channel)) not in get_meters():
        # the function flash() is part of the flask system and lets us
        # register error/warning messages that should be shown on the
        # web page.
        flash(f"The meter {meter} with channel {channel} does not exist.")
        return []

    # this just generates a fixed set of measurement values
    # to have something to show...
    measurements = []
    time = 1624537020
    for _ in range(20):
        date = datetime.datetime.fromtimestamp(time)
        value = time % 27
        measurements.append((date, value, UNITS[0]))
        time = time - 10 * 60
    return measurements

# @app.route registers a handler for a specific URL
# in this case the URL / (i.e. the root of the server)

@app.route("/")
def start_page():
    meters = mmeters()
    return render_template("start.html", meters=meters)

# using @app.route with <something> makes "something" into
# a path variable. In the case /meter/1234/channel/5678
# the meter-argument would be set to (the string!) 1234
# and channel to 5678.

@app.route("/meter/<meter>/channel/<channel>")
def show_measurements(meter, channel):
    #measurements = get_measurements(meter, channel)
    #```
    list_3 = read_and_split_string()
    measurements.append((list_3[1], list_3[3], UNITS[0]))
    meter = list_[0]
    channel = list_[2]
    #```
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)


from flask import Flask, render_template, flash
import datetime
import time

txtPath = "D:/Documents/Tempprojekt/flask-example/vizualisr/temperature.txt"

#Sätt miljövariabel till: $Env:FLASK_APP="vizualisr"

# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)

def get_data(data, n):
    test = 0
    with open(txtPath,"r") as file:
        temperature_data = file.readlines()
        for line in temperature_data:
            id, i, t, d, u = split_data(line)
            id = str(id)
            d = float(d)
            d = d/1000
            t = int(t, 16)
            t = datetime.datetime.fromtimestamp(t)
            if n == "id_and_index":
                if (id,i) not in data:    
                    data.append((id, i))
            if n == "all data":
                data.append((id, i, t, d, u))
    return data

def get_meters():
    list_of_sensors = []
    list_of_sensors = get_data(list_of_sensors,"id_and_index")
    return list_of_sensors

def split_data(line):
    line_list = line.split()
    sensor_id = line_list[0]
    time = line_list[1]
    index = line_list[2]
    data = line_list[3]
    unit = line_list[4]
    return (sensor_id, index, time, data, unit)

def get_measurements(meter, channel):
    measurements = []
    #meter = int(meter, 16)
    channel = int(channel, 16)
    measurements = get_data(measurements,"all data")
    measurements = [id_and_index[2:] for id_and_index in measurements]
    measurements.reverse()
    return measurements

@app.route("/")
def start_page():
    meters = get_meters()
    return render_template("start.html", meters=meters)

@app.route("/meter/<meter>/channel/<channel>")
def show_measurements(meter, channel):
    measurements = get_measurements(meter, channel)
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)    



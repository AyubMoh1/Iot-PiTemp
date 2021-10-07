from flask import Flask, render_template, flash
import datetime
import time

#Anger sökvägen där textfilen med data ligger 
txtPath = "D:/Documents/Tempprojekt/flask-example/vizualisr/temperature.txt"

#Sätt miljövariabel till: $Env:FLASK_APP="vizualisr"

# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)

#Funktionen öppnar textfilen med data och skikcar varje rad till en 
#funktion som delar upp varje textrad i fem delar
#Basserat på ett index n skickar den tillbaka sensorID och kanalindex, 
#eller tidsstämpel, temperatur och enhet
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
            if n == "time_temperature_unit":
                data.append((t, d, u))
    return data

#Funktionen kallar till funtionen get_data som, basserat på en textsträng
#appendar en lista med sensorID och kanalindex. Listan returneas sedan. 
def get_meters():
    list_of_sensors = []
    list_of_sensors = get_data(list_of_sensors,"id_and_index")
    return list_of_sensors

#Funktionen tar in en textsträng och lägger in alla orden i textsträngen 
# i en separat lista. Listan delas sedan upp och returneras som en tuple.
#En förbättrad variant av denna hade kanske kunnat lösas med en for-loop.
def split_data(line):
    line_list = line.split()
    sensor_id = line_list[0]
    time = line_list[1]
    index = line_list[2]
    data = line_list[3]
    unit = line_list[4]
    return (sensor_id, index, time, data, unit)

#Denna funktionen anropar funktionen get data med en variabel som gör att funktionen returnerar 
# tidsslag, temperatur och enhet. Datan läggs in i en lista som till sist vänds uppochner
#Listan vänds uppochner för att den nya datan skall visas högst upp i visningsprogrammet.
#Funktionen returnerar den korrigerade listan. 
def get_measurements(meter, channel):
    measurements = []
    measurements = get_data(measurements,"time_temperature_unit")
    measurements.reverse()
    return measurements

@app.route("/")
#Funktionen sätter upp en visningssida som radar upp samtliga sensorer som detekteras i en textfil. 
def start_page():
    meters = get_meters()
    return render_template("start.html", meters=meters)

@app.route("/meter/<meter>/channel/<channel>")
#Funktionen presenterar datan i webbserverns visningssida
def show_measurements(meter, channel):
    measurements = get_measurements(meter, channel)
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)    

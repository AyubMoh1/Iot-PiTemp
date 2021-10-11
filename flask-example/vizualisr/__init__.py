from flask import Flask, render_template, flash
import datetime
import time

#txtPath = "C:/Users/chartedge/Desktop/Iot-PiTemp-main/flask-example/vizualisr/temperature.txt" #Ayub's dator
txtPath = "D:/Documents/Tempprojekt/flask-example/vizualisr/temperature.txt" #Alex's dator

#Sätt miljövariabel till: $Env:FLASK_APP="vizualisr"

# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)

#Funktionen öppnar en textfil med mätdata och läser in allt och omformaterar informationen till en önskvärd form. 
def get_data():
    list_of_tuples = []
    with open(txtPath,"r") as file: #Öppnar och läser textfilen som anges i txtPath
        all_lines_in_file = file.readlines() #Tar in samtliga rader från filen
        for line in all_lines_in_file: #Loopen stegar igenom alla rader
            sensor_id, channel, time, temperature, unit = split_data(line) #Delar upp rad
            temperature = float(temperature) # Omvandlar temperaturen till flyttal
            temperature = temperature/1000 #Omformaterar temperaturen efter att den multiplicerats med 1000 innan den skickats via MQTT
            time = int(time, 16) #Omtolkar tiden från strängformat till heltalsformat
            time = datetime.datetime.fromtimestamp(time) #Omvandlar tiden från time-since-epoch-format till faktisk datum och tid. 
            list_of_tuples.append((sensor_id, channel, time, temperature, unit)) #Lägger till all data från raden som en tuple, längst bak i en lista
    return list_of_tuples

#Funktionens syfte är att returnera en lista över de sensorer som används och de eventuella mätkanaler de i sin tur använder.
def get_meters():
    identification = get_data() #Tar in all data från textfilen: id, kanal, tidsslag, temperatur och enhet.  
    identification = [id_and_index[:2] for id_and_index in identification] #Sollar bort allt som inte är id och kanal
    return [t for t in (set(tuple(i) for i in identification))] #Tar bort dubbletter och returnerar

#Funktionen delar upp en orden i en textsträng och returnerar dem som en tuple
def split_data(line):
    separated_line = line.split()
    sensor_id = separated_line[0]
    time = separated_line[1]
    channel = separated_line[2]
    temperature = separated_line[3]
    unit = separated_line[4]
    return (sensor_id, channel, time, temperature, unit)

#Funktionen hämtar en lista av tupler, filtrerar den, och vänder på den
def get_measurements(sensor_id, channel_index):
    measurements = get_data()
    measurements = [ m for m in measurements if m[0] == sensor_id and m[1] == channel_index ] #Tar bort alla tuples där sensor_id och channel_index inte matchar
    measurements = [id_and_index[2:] for id_and_index in measurements] #Tar bort allt utom de två främsta elementen i varje tuple.
    measurements.reverse() #Vänder på listan så att den senaste datan presenteras först
    return measurements

@app.route("/")
#Funktionen sätter upp första sidan av visningsprogrammet där alla olika sensorer presenteras med respektive kanaler.
def start_page():
    meters = get_meters()
    return render_template("start.html", meters=meters)

@app.route("/meter/<meter>/channel/<channel>")
#Funktionen presenterar all mätdata på visningsprogrammets andra sida
def show_measurements(meter, channel):
    measurements = get_measurements(meter, channel)
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)  

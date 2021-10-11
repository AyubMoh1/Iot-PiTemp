#Modul som läser och omvandlar värdet från en temperaturgivare
import tempguage as temperature
#Modul som hanterar MQTT-implementation
import paho.mqtt.client as mqtt
import time

#Skapar en MQTT-klient
client = mqtt.Client()

topic = "measurement/280000095c43dd" #Anger topic

#Ansluter till en broker --> HiveMQ idetta fallet
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
#client.connect("192.168.1.27",port=1883, keepalive=60) #Ayub's bärbara
client.connect("192.168.0.155",port=1883, keepalive=60) #Alex stationära
#client.connect("192.168.1.40", port=1883, keepalive=60) #Jad's bärbara

#Startar bakgrundsprocess som hanterar kommunikation med brokern
client.loop_start()

while True:
    temperature_sensor_data = temperature.sensor_package() #Hämtar data från filen temperatureguage.py
    msg = client.publish(topic, payload=temperature_sensor_data, qos=1) #Publicerar data på MQTT-servern, på angiven topic
    time.sleep(60) #Skickar data en gång varje minut, enligt spec.

#Väntar tills meddelandet är publicerat
msg.wait_for_publish()
#Bryter koppling till broker
client.disconnect()

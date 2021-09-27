"""Author: Alexander Mörch"""

#Modul som läser och omvandlar värdet från en temperaturgivare
import dht as temp
#Modul som hanterar MQTT-implementation
import paho.mqtt.client as mqtt
import time

#Skapar en MQTT-klient
client = mqtt.Client()

#Ansluter till en broker --> HiveMQ idetta fallet
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.connect("192.168.1.204",port=1883, keepalive=60)

#Startar bakgrundsprocess som hanterar kommunikation med brokern
client.loop_start()

while True:
    #Läser data från temperaturgivaren --> Se tempguage-modulen
    var = temp.result.temperature

    #Anger topic, vad som skall skickas, och quality of service
    msg1 = client.publish("yrgo/ela20/Dark/hello", payload=var, qos=1)

    #Väntar en sekund
    time.sleep(1)

#Väntar tills meddelandet är publicerat
msg1.wait_for_publish()
#Bryter koppling till broker
client.disconnect()

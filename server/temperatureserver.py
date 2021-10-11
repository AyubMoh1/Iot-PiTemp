import struct
import paho.mqtt.client as mqtt
import datetime

#Denna filen tar in binärdata från en angiven topic och skriver in datan i en textfil

txtPath = "D:/Documents/Tempprojekt/flask-example/vizualisr/temperature.txt" #Anger sökväg till texfilen temperature.txt.
topic = "measurement/280000095c43dd" # Anger topic för MQTT.

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic, qos=1) #Sätter upp en subscription på angivet topic.

def on_message(client, userdata, msg):
    a, b, c, d, e = struct.unpack("QIBIB", msg.payload) #Packar upp binärdata i fem variabler 
    with open(txtPath, "a") as file:
        file.write(f"{a:x} {b:X} {c:x} {d:x} {e:x}\n") #Omvandlar alla värden till strängar och skriver ut dem i en textfil.


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.0.155", port=1883, keepalive=60) 
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.connect("localhost", port=1883, keepalive=60)
client.loop_forever()

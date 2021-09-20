"""Alexander Mörch"""

import paho.mqtt.client as mqtt

#Sätter topic och quality of service
def on_connect(client, userdata, flags, rc):
    client.subscribe("yrgo/ela20/Dark/hello", qos=1)

#Skriver ut meddelande på terminalen
def on_message(client, userdata, msg):
    print(f"{float(msg.payload)}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.0.155", port=1883, keepalive=60)
client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.loop_forever()

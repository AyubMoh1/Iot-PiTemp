import struct
import paho.mqtt.client as mqtt
import datetime

txtPath = "D:/Documents/Tempprojekt/flask-example/vizualisr/temperature.txt"

def on_connect(client, userdata, flags, rc):
    client.subscribe("sensors/temperature/channel1", qos=1)
    #client.subscribe("measurement/280000095c43dd", qos=1)


def on_message(client, userdata, msg):
    a, b, c, d, e = struct.unpack("QIBIB", msg.payload)
    with open(txtPath, "a") as file:
        file.write(f"{a:x} {b:X} {c:x} {d:x} {e:x}\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.0.155", port=1883, keepalive=60) 
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.connect("localhost", port=1883, keepalive=60)
client.loop_forever()

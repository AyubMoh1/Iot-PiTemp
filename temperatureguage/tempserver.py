import struct
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("sensors/temperature/channel1", qos=1)

def on_message(client, userdata, msg):
    #print(f"{float(msg.payload)}")
    #var = msg.payload
    #var1 = var.decode("UTF-8") 
    
    with open("temperature.txt", "a") as file:
        #file.write(f"{var1}\n")   
        file.write(f"{msg.payload}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.0.155", port=1883, keepalive=60) 
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.connect("localhost", port=1883, keepalive=60)
client.loop_forever()


import paho.mqtt.client as mqtt
import time 

# Create a MQTT client and register a callback
# for connect events
client = mqtt.Client()
client.on_connect = on_connect

# Connect to a broker
client.connect("localhost", port=1883, keepalive=60)

# Start a background loop that handles all
# communication with the MQTT broker
client.loop_start()

# send a random value every second
while True:
    client.publish("some/topic", payload=data, qos=1)
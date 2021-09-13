import paho.mqtt.client as mqtt
import struct

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()
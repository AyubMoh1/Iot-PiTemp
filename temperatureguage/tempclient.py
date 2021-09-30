#Modul som läser och omvandlar värdet från en temperaturgivare
import tempguage as temp
#Modul som hanterar MQTT-implementation
import paho.mqtt.client as mqtt
import time

#Skapar en MQTT-klient
client = mqtt.Client()

#Ansluter till en broker --> HiveMQ idetta fallet
#client.connect("broker.hivemq.com", port=1883, keepalive=60)
client.connect("192.168.0.155",port=1883, keepalive=60)

#Startar bakgrundsprocess som hanterar kommunikation med brokern
client.loop_start()

while True:

    var = temp.sensor_package()

    msg1 = client.publish("sensors/temperature/channel1", payload=var, qos=1)

    #Väntar en sekund
    time.sleep(1)

#Väntar tills meddelandet är publicerat
msg1.wait_for_publish()
#Bryter koppling till broker
client.disconnect()

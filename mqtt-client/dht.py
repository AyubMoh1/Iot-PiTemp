import dht11
import RPi.GPIO as GPIO
import sys
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# read data using GPIO pin 3 (i.e. rpi pin 5)
instance = dht11.DHT11(pin = 3)
result = instance.read()
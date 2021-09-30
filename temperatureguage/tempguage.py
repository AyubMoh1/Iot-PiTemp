"""Author Alexander Mörch"""

import os
import glob
import time
import datetime
import struct

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Hittar temperaturgivarens sökväg
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
device_ID = device_folder.replace(base_dir,'')

#def get_sensor_ID():
#    with open('/sys/bus/w1/devices/28-0000095c43dd/id',"r") as file:
#        return file.readline()

#Läser data från filen där temperaturdatan sparas
def read_temperature_raw():
    with open(device_file, "r") as temp_read_file:
        return temp_read_file.readlines()

#Omvandlar temperaturdatan till något mer läsbart
def read_temperature():
    lines = read_temperature_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def sensor_package():
    temperature = read_temperature()
    tid = get_datetime_string()
    A = format_frame(device_ID, tid ,temperature)
    return bytearray(A, "UTF-8")

#Tar in
def format_frame(A,B,C):
    return 'SensorID: ' + A + ' Time: '+ B + ' Temperature: ' + str(C) + ' C'

def get_datetime_string():
    dt = datetime.datetime.now()
    return dt.strftime("%d/%m/%Y %H:%M:%S")

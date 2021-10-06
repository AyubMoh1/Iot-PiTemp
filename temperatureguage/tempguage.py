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
device_ID = device_folder.replace(base_dir,'') #Hittar ID
S_ID = device_ID.replace('-','') #Tar bort '-' från ID
S_ID = int(S_ID, 16)

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
        temp_c = temp_string #float(temp_string) / 1000.0
        return temp_c

def sensor_package():
    unit = "C"
    unit = int(unit, 16)
    index = int(1)
    temperature = int(read_temperature(), 16)
    tid = get_datetime_string()
    return struct.pack('QIBIB', S_ID, tid, index, temperature, unit)

def get_datetime_string():
    date_time = int(time.time())
    return date_time

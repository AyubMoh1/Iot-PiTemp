
import os
import glob
import time
import datetime
import struct

#Sätter miljövariabler för entådsbuss 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Hittar temperaturgivarens sökväg
base_dir = '/sys/bus/w1/devices/' #Anger grunden till givarens sökväg
device_folder = glob.glob(base_dir + '28*')[0] #Söker efter ett filnamn som börjar på 28
device_file = device_folder + '/w1_slave' #Sätter samman sökväg till filen som innehåller rå data
device_ID = device_folder.replace(base_dir,'') #Hittar givarens ID
S_ID_str = device_ID.replace('-','') #Tar bort '-' från ID
S_ID = int(S_ID_str, 16) #Omvandlar till heltal

#Läser data från filen där den råa temperaturdatan sparas
def read_temperature_raw():
    with open(device_file, "r") as temp_read_file:
        return temp_read_file.readlines()

#Omvandlar temperaturdatan till något mer läsbart
def read_temperature():
    lines = read_temperature_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temperature_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = temp_string #float(temp_string) / 1000.0
        return temp_c

#Funktioner samlar ihop och formaterar data. Datan packas ihop och returneras sedan på binärform
def sensor_package():
    unit = "C"
    unit = int(unit, 16) 
    index = int(1)
    temperature = int(read_temperature(), 16)   
    time = get_datetime_string()
    return struct.pack('QIBIB', S_ID, time, index, temperature, unit)

#Funktionen hämtar time since epoch
def get_datetime_string():
    date_time = int(time.time())
    return date_time


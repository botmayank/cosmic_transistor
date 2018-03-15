#!/usr/bin/python
import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
import spidev

LOG_FILE = "/media/pi/MISHO/DATA/data_log.csv"

PINS = [27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 18,\
         23, 24, 25, 8, 7, 12, 16, 20, 21]

CHANNELS = [0,1,2,3,4]

GPIO.setmode(GPIO.BCM)
mosfet_header = []

SLEEP_TIME = 10 #Seconds

spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

for i in range(len(PINS)):
    GPIO.setup(PINS[i], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    mosfet_header.append("MOSFET" + str(i+1))

csv_header = ",".join(mosfet_header)
# print csv_header

csv_header = "Time," + csv_header + "\n"
# print csv_header

file = open(LOG_FILE, "a")
if os.stat(LOG_FILE).st_size == 0:
    file.write(csv_header)

while True:
    now = datetime.now()
    reading = []
    setting = []

    for i in range(len(PINS)):
        reading.append(str(GPIO.input(PINS[i])))

    for i in range(len(CHANNELS)):
        setting.append(str(readadc(CHANNELS[i])))

    config_reading = ",".join(setting) + "\n"

    csv_reading = str(now) + ", " + ",".join(reading) + "\n" 

    print "-------------PINS READING------------------"
    print csv_reading

    print "------------CONFIG READING-----------------"
    print config_reading

    file.write(csv_reading)
      
    file.flush()
    time.sleep(SLEEP_TIME)

file.close()
GPIO.cleanup()

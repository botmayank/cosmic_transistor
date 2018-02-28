#!/usr/bin/python
import os
import time
from datetime import datetime
import RPi.GPIO as GPIO

LOG_FILE = "/media/pi/MISHO/data_log.csv"

PINS = [27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 18,\
         23, 24, 25, 8, 7, 12, 16, 20, 21]

SLEEP_TIME = 10 #Seconds

GPIO.setmode(GPIO.BCM)

mosfet_header = []

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
    for i in range(len(PINS)):
        reading.append(str(GPIO.input(PINS[i])))

    csv_reading = str(now) + ", " + ",".join(reading) + "\n"    
    file.flush()
    time.sleep(SLEEP_TIME)

file.close()
GPIO.cleanup()

#!/usr/bin/python
import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
import spidev

# PINS = [27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 18,\
         # 23, 24, 25, 8, 7, 12, 16, 20, 21]

PINS = [27, 22, 5, 6, 13, 19, 26, 18,\
         23, 24, 25, 7, 12, 16, 20, 21]

GATE_CHANNEL = 0
SUPPLY_CHANNEL = 1

GATE_THRESH_HIGH = 955

GATE_THRESH_LOW_UPPER = 508
GATE_THRESH_LOW_LOWER = 365

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

def modify_gate_reading(data):
    if data >= GATE_THRESH_HIGH:        
        data = 0
    elif (GATE_THRESH_LOW_LOWER <= data <= GATE_THRESH_LOW_UPPER):
        data = -5
    return data

def modify_supply_reading(data):
    # supply voltage: 1200V / 10 bit ADC: 1023 ==> 1200/1023=1.173
    return data*1.173

for i in range(len(PINS)):
    GPIO.setup(PINS[i], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    mosfet_header.append("MOSFET" + str(i+1))

csv_header = ",".join(mosfet_header)
# print csv_header

csv_header = csv_header + ",Gate Voltage,Supply Voltage"

csv_header = "Time," + csv_header + "\n"
# print csv_header

setting = []

gate_data = readadc(GATE_CHANNEL)
supply_data = readadc(SUPPLY_CHANNEL)

gate_data = modify_gate_reading(gate_data)
supply_data = modify_supply_reading(supply_data)

setting.append(str(gate_data))
setting.append(str(supply_data))

config_reading = ",".join(setting)

FILENAME = "data_log_" + str(supply_data) + "_" + str(datetime.now()) + ".csv"
LOG_FILE = "/home/pi/adc_test/Data/" + FILENAME

file = open(LOG_FILE, "a")
if os.stat(LOG_FILE).st_size == 0:
    file.write(csv_header)

while True:
    now = datetime.now()
    reading = []

    for i in range(len(PINS)):
        reading.append(str(GPIO.input(PINS[i])))

    pins_reading = ",".join(reading)

    print "-------------PINS READING------------------"
    print pins_reading

    print "------------CONFIG READING-----------------"
    print config_reading

    csv_reading = str(now) + ","+ pins_reading +"," + config_reading + "\n"

    file.write(csv_reading)
      
    file.flush()
    time.sleep(SLEEP_TIME)

file.close()
GPIO.cleanup()

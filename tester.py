import RPi.GPIO as GPIO
import os
import time
from datetime import datetime

PIN1 = 27
PIN2 = 22
PIN3 = 10
PIN4 = 9
PIN5 = 11
PIN6 = 5
PIN7 = 6
PIN8 = 13
PIN9 = 19
PIN10 = 26
PIN11 = 18
PIN12 = 23
PIN13 = 24
PIN14 = 25
PIN15 = 8
PIN16 = 7
PIN17 = 12
PIN18 = 16
PIN19 = 20
PIN20 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file = open("/media/pi/MISHO/data_log.csv", "a") 

if os.stat("/media/pi/MISHO/data_log.csv").st_size == 0:
    file.write("Time,MOSEFT1,MOSFET2,MOSFET3,MOSFET4,MOSFET5,MOSFET6,MOSFET7,MOSFET8,MOSFET9,MOSFET10,MOSFET11,MOSFET12,MOSFET13,MOSFET14,MOSFET15,MOSFET16,MOSFET17,MOSFET18,MOSFET19,MOSFET20\n")

while True:
    now = datetime.now()
    pin1_status = GPIO.input(PIN1)
    pin2_status = GPIO.input(PIN2)
    pin3_status = GPIO.input(PIN3)
    pin4_status = GPIO.input(PIN4)
    pin5_status = GPIO.input(PIN5)
    pin6_status = GPIO.input(PIN6)
    pin7_status = GPIO.input(PIN7)
    pin8_status = GPIO.input(PIN8)
    pin9_status = GPIO.input(PIN9)
    pin10_status = GPIO.input(PIN10)
    pin11_status = GPIO.input(PIN11)
    pin12_status = GPIO.input(PIN12)
    pin13_status = GPIO.input(PIN13)
    pin14_status = GPIO.input(PIN14)
    pin15_status = GPIO.input(PIN15)
    pin16_status = GPIO.input(PIN16)
    pin17_status = GPIO.input(PIN17)
    pin18_status = GPIO.input(PIN18)
    pin19_status = GPIO.input(PIN19)
    pin20_status = GPIO.input(PIN20)
    file.write(str(now)+",   "+str(pin1_status)+","+str(pin2_status)+","+str(pin3_status)+","+str(pin4_status)+","+str(pin5_status)+","+str(pin6_status)+","+str(pin7_status)+","+str(pin8_status)+","+str(pin9_status)+","+str(pin10_status)+","+str(pin11_status)+","+str(pin12_status)+","+str(pin13_status)+","+str(pin14_status)+","+str(pin15_status)+","+str(pin16_status)+","+str(pin17_status)+","+str(pin18_status)+","+str(pin19_status)+","+str(pin20_status)+"\n")
    file.flush()
    time.sleep(10)
file.close()
GPIO.cleanup()


#!/usr/bin/python
 
import spidev
import time

#Define Variables
delay = 0.5
channel_0 = 0
channel_1 = 1
#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
 
while True:
    val_0 = readadc(channel_0)
    val_1 = readadc(channel_1)
    print "---------------------------------------"
    print("ADC Values : %d  %d" %(val_0,val_1))
    time.sleep(delay)

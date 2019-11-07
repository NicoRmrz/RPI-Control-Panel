# ADS79241.py
# Read values from ADC

import smbus
import time

bus = smbus.SMBus(1) # using i2c bus 1
i2c_address = 0x48
control_byte0 = 0x00 # to read channel 0
control_byte1 = 0x01 # to read channel 1
control_byte2 = 0x02 # to read channel 2
control_byte3 = 0x03 # to read channel 3

while (1):
    data = bus.read_byte_data(i2c_address, control_byte0)
    print  ("s:" + data)
 
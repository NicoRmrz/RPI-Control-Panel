import board
import busio
import time
from time import sleep
import datetime
import os
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

i2c_address = 0x49

# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- ADS79241 ADC Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class ADC_thread(QThread):
	ADC_meas = pyqtSignal(int, int) 
    
	def __init__(self):
		QThread.__init__(self)
		
		# Create i2c
		i2c = busio.I2C(board.SCL, board.SDA)
		
		# Create ADS1115 ADC (16-bit) instance
		self.ads = ADS.ADS1115(i2c, address=i2c_address)

		# set Channel
		# 	chan0 - bottom draw wire sensor
		# 	chan1 - verticle tower draw wire sensor
		self.chan0 = AnalogIn(self.ads, ADS.P0)
		self.chan1 = AnalogIn(self.ads, ADS.P1)

		# Set Gain
		# 	2/3 = +/- 6.144V
		# 	1   = +/- 4.096V
		# 	2   = +/- 2.048V
		# 	4   = +/- 1.024V
		# 	8   = +/- 0.512V
		# 	16  = +/- 0.256V
		self.ads.gain = 1
		
        
	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):

			# ~ floorSensorADC_V = (1000000 * self.chan0.voltage * 0.7)
			# ~ towerSensorADC_V = (1000000 * self.chan1.voltage)
			
			# ~ floorSensorADC_V = ((self.chan0.voltage*14.166) * 1000)
			# ~ towerSensorADC_V = (1000 * self.chan1.voltage * .474)
			
			# ~ floorSensorADC_V = self.chan0.value
			# ~ towerSensorADC_V = self.chan1.value
			
			# Value converted to mm
			floorSensorADC_V = abs(self.chan0.value * 0.45)
			towerSensorADC_V = self.chan1.value * 2.75
			
			# ~ print("Channel 0: " + str(floorSensorADC_V) + " v  Channel 1: " + str(towerSensorADC_V) + " v")

			
			self.ADC_meas.emit(floorSensorADC_V, towerSensorADC_V)
			time.sleep(0.2)



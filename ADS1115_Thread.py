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
		self.chan0 = AnalogIn(self.ads, ADS.P0)
		self.chan1 = AnalogIn(self.ads, ADS.P1)
		self.chan2 = AnalogIn(self.ads, ADS.P2)

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

			# ~ print(str(self.chan1.value) + ", " + str(self.chan1.voltage))
			print(self.chan0.value, self.chan0.voltage)
			print(self.chan1.value, self.chan1.voltage)
			print(self.chan2.value, self.chan2.voltage)
			# ~ print(self.chan1.value)
			# ~ LeftRightSlider = self.adc.read_adc(0, gain=self.GAIN)
			# ~ UpDownSlider = self.adc.read_adc(1, gain=self.GAIN)
			# ~ x = self.adc.read_adc(2, gain=self.GAIN)
			# ~ y = self.adc.read_adc(3, gain=self.GAIN)
			
			# ~ self.ADC_meas.emit(LeftRightSlider, UpDownSlider)
			# ~ print(LeftRightSlider + ", " + UpDownSlider + ", " + x+ ", " +y)

            
			time.sleep(0.5)



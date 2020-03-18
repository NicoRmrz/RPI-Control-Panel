import time
from time import sleep
import datetime
import os
import Adafruit	_ADS1x15
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

i2c_address = 0x49

# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- ADS79241 ADC Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class ADC_thread(QThread):
	ADC_meas = pyqtSignal(int, int) 
    
	def __init__(self):
		QThread.__init__(self)
		
		# I2C Configuration


        
	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):

			# ~ self.ADC_meas.emit(LeftRightSlider, UpDownSlider)
			

            
			time.sleep(0.2)



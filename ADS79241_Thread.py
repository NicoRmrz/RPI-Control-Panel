import time
from time import sleep
import datetime
import os
import smbus
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

i2c_address = 0x49
ADC_ch0 = 0x02
ADC_ch1 = 0x04
ADC_ch2 = 0x06
ADC_ch3 = 0x08

IDLE = 0x00
AWAKE = 0x80
AUTO_SCAN = 0xCC
AUTO_SINGLE = 0xC4
MANUAL_SCAN = 0xC8


# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- ADS79241 ADC Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class ADC_thread(QThread):
	doneFlag = pyqtSignal(str) 
    
	def __init__(self):
		QThread.__init__(self)
		
		# I2C Configuration
		self.bus = smbus.SMBus(1)

		self.bus.write_byte_data(i2c_address, 0, IDLE)
		# ~ self.bus.write_byte_data(i2c_address, 0, 0x20)
		self.bus.write_byte_data(i2c_address, 0, AUTO_SCAN)
		self.exitProgram = False

	
	
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter
	
	# ~ def read_word
        
	def run(self):
		# ~ self.setPriority(QThread.HighestPriority)

		while (1):

			# ~ data1 = self.bus.read_byte_data(i2c_address, ADC_ch0)
			# ~ data2 = self.bus.read_byte_data(i2c_address, ADC_ch1)
			# ~ data3 = self.bus.read_byte_data(i2c_address, ADC_ch2)
			data4 = self.bus.read_byte_data(i2c_address, ADC_ch3)
			val = ((data4 << 4)) << 1
			val2 = (val * 2.2)/4096
			print("ch3: " + str(data4) )

			# ~ data4 = self.bus.read_i2c_block_data(i2c_address, 0x00,2)
			# ~ val = ((data4[0] << 4) | (data4[1] >> 4)) << 1
			# ~ val2 = (val * 2.2)/4096

			# ~ data3 = self.bus.read_i2c_block_data(i2c_address, 0x00,2)
			# ~ val = ((data3[0] << 4) | (data3[1] >> 4)) << 1
			# ~ val2 = (val * 2.2)/4096

			
			# ~ print("ch0: " + str(data1) )
			# ~ print("ch1: " + str(data2) )
			# ~ print("ch2: " + str(data3) )
			print("val: " + str(val) )
			print("val2: " + str(val2) )
			# ~ print("ch3: " + str(data4) )
			
							

			
			if(self.exitProgram == True):
				self.bus.write_byte_data(i2c_address, 0, IDLE)
				self.exitProgram = False
				break
            
			time.sleep(0.5)

# ~ ADC = ADC_thread()
# ~ ADC.start() 

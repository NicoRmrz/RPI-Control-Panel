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
	ADC_meas = pyqtSignal(int, int) 
    
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
	
	# ~ def twosComp(self, val, bits):
		# ~ if ((val &(1 << (bits -1))) !=0)
			# ~ val = val- (1 <<bits)
		# ~ return val
        
	def run(self):
		# ~ self.setPriority(QThread.HighestPriority)

		while (1):

			# ~ data0 = self.bus.read_byte_data(i2c_address, ADC_ch0)
			# ~ data1 = self.bus.read_byte_data(i2c_address, ADC_ch1)
			# ~ data12 = self.bus.read_byte_data(i2c_address, ADC_ch1)
			# ~ data2 = self.bus.read_byte_data(i2c_address, ADC_ch2)
			# ~ data3 = self.bus.read_byte_data(i2c_address, ADC_ch3)
			
			
			# Read 2 bytes
			data1 = self.bus.read_word_data(i2c_address, ADC_ch1)
			data2 = self.bus.read_word_data(i2c_address, ADC_ch2)
			
			# Exchange high and low bytes
			ch1_ADC = ((data1 & 0xFF) << 8) | ((data1 & 0xFF00) >> 8)
			ch2_ADC = ((data2 & 0xFF) << 8) | ((data2 & 0xFF00) >> 8)
			
			# Ignore four least sig bits
			ch1_ADC = ch1_ADC >> 4
			ch2_ADC = ch2_ADC >> 4
			
			# ~ ch1_comp = self.twosComp(ch1_ADC,12)
			# ~ ch2_comp = self.twosComp(ch2_ADC,12)
			
			# ~ print("ch0: " + str(data0) )
			# ~ print("ch1: " + str(data1) )
			# ~ print("ch2: " + str(data2) )
			# ~ print("ch3: " + str(data3) )
			
			
			# ~ LeftRightSlider = ((1000 * data1)/ 2 ** 8 - data1)/ 0.476
			# ~ LeftRightSlider = ((1000 * data1)/ 2 ** 12 - data1)/ 0.476
			# ~ LeftRightSlider = ((1000 * data1)/ (2 ** 12 - data1))/ 0.476
			# ~ LeftRightSlider = ((1000 * data1)/ (4096 - data1))/ 0.476
			LeftRightSlider = ((1000 * ch1_ADC)/ (4096 - ch1_ADC))/ 0.476
			# ~ LeftRightSlider = ((1000 * ch1_ADC)/ (2 ** 12 - ch1_ADC))/ 0.476
			
			# ~ UpDownSlider = ((10000 * data2)/ (2**12 - data2))/ 7.87
			# ~ UpDownSlider = ((10000 * data2)/ (4096 - data2))/ 7.87
			UpDownSlider = ((10000 * ch2_ADC)/ (4096 - ch2_ADC))/ 7.87
			# ~ UpDownSlider = ((10000 * ch2_ADC)/ (2**12 - ch2_ADC))/ 7.87
			
			self.ADC_meas.emit(LeftRightSlider, UpDownSlider)
			# ~ self.ADC_meas.emit(ch1_ADC, ch2_ADC)
			# ~ self.ADC_meas.emit(ch1_comp, ch2_comp)

			
			if(self.exitProgram == True):
				self.bus.write_byte_data(i2c_address, 0, IDLE)
				self.exitProgram = False
				break
            
			time.sleep(0.2)



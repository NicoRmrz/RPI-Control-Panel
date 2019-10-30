import time
from time import sleep
import datetime
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import RPi.GPIO as GPIO

RSidePB1 = 9
RSidePB2 = 10
RSidePB3 = 27
RSidePB4 = 17
RSidePB5 = 22
LSidePB1 = 26
LSidePB2 = 19
LSidePB3 = 6
LSidePB4 = 11
LSidePB5 = 13

RlyCtrl1 = 16
RlytCtrl2 = 12
RlyCtrl3 = 7
RlyCtrl4 = 8
RlyCtrl5 = 25
RlyCtrl6 = 24
RlyCtrl7 = 23
RlyCtrl8 = 18
RlyCtrl9 = 15
RlyCtrl10 = 14

# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- GPIO Control Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class GPIO_control(QThread):
	doneFlag1 = pyqtSignal(str) 
    
	def __init__(selfs):
		QThread.__init__(self)
		
		# GPIO Configuration
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(RSidePB1,  GPIO.IN)
        GPIO.setup(RSidePB2,  GPIO.IN)
        GPIO.setup(RSidePB3,  GPIO.IN)
        GPIO.setup(RSidePB4,  GPIO.IN)
        GPIO.setup(RSidePB5,  GPIO.IN)

        GPIO.setup(LSidePB1,  GPIO.IN)
        GPIO.setup(LSidePB2,  GPIO.IN)
        GPIO.setup(LSidePB3,  GPIO.IN)
        GPIO.setup(LSidePB4,  GPIO.IN)
        GPIO.setup(LSidePB5,  GPIO.IN)

        GPIO.setup(RlyCtrl1,  GPIO.OUT)
        GPIO.setup(RlyCtrl2,  GPIO.OUT)
        GPIO.setup(RlyCtrl3,  GPIO.OUT)
        GPIO.setup(RlyCtrl4,  GPIO.OUT)
        GPIO.setup(RlyCtrl5,  GPIO.OUT)
        GPIO.setup(RlyCtrl6,  GPIO.OUT)
        GPIO.setup(RlyCtrl7,  GPIO.OUT)
        GPIO.setup(RlyCtrl8,  GPIO.OUT)
        GPIO.setup(RlyCtrl9,  GPIO.OUT)
        GPIO.setup(RlyCtrl10,  GPIO.OUT)

		self.setLow = False
		self.exitProgram = False
	
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter
		
	#Sets all GPIO pins Low
	def	setAllLow(self, state):
		self.setLow = state
        
	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):

			print("R PB 1: " + str(GPIO.input(RSidePB1)))

			if self.setLow == True:

				self.GPIO.output(Relay1_40, GPIO.LOW)
				self.GPIO.output(Relay1_60, GPIO.LOW)
				self.GPIO.output(Relay1_500, GPIO.LOW)
				self.GPIO.output(Relay1_1k, GPIO.LOW)

				self.setLow = False
				

			if self.set40 == True:
				if self.GPIO.input(Relay1_40) == 0:
					self.GPIO.output(Relay1_40, GPIO.HIGH)
					self.GPIO.output(Relay1_60, GPIO.LOW)
					self.GPIO.output(Relay1_500, GPIO.LOW)
					self.GPIO.output(Relay1_1k, GPIO.LOW)
						

				else: 
					self.GPIO.output(Relay1_40, GPIO.LOW)
					self.doneFlag1.emit("40L")
				
				self.set40 = False
		
			
			if(self.exitProgram == True):
				self.exitProgram = False
				break
            
			# time.sleep(0.2)


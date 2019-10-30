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

        GPIO.setup(RSidePB1,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RSidePB2,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RSidePB3,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RSidePB4,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RSidePB5,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.setup(LSidePB1,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(LSidePB2,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(LSidePB3,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(LSidePB4,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(LSidePB5,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

		self.run1 = False
		self.run2 = False
		self.run3 = False
		self.run4 = False
		self.run5 = False
	
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter
		
	#Sets all GPIO pins Low
	def	setAllLow(self, state):
		self.setLow = state
        
	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):


			if self.setLow == True:

				self.GPIO.output(RlyCtrl1, GPIO.LOW)
				self.GPIO.output(RlyCtrl2, GPIO.LOW)
				self.GPIO.output(RlyCtrl3, GPIO.LOW)
				self.GPIO.output(RlyCtrl4, GPIO.LOW)
				self.GPIO.output(RlyCtrl5, GPIO.LOW)
				self.GPIO.output(RlyCtrl6, GPIO.LOW)
				self.GPIO.output(RlyCtrl7, GPIO.LOW)
				self.GPIO.output(RlyCtrl8, GPIO.LOW)
				self.GPIO.output(RlyCtrl9, GPIO.LOW)
				self.GPIO.output(RlyCtrl10, GPIO.LOW)

				self.setLow = False
				
			#Push Button 1
			if (GPIO.input(LSidePB1) or GPIO.input(RSidePB1)):
				if ((self.run2 and self.run3 and self.run4 and self.run5) != True):
					self.run1 = True
								#set relay
					
			else:
				self.run1 = False
				# turn off		
			
			#Push Button 2
			if (GPIO.input(LSidePB2) or GPIO.input(RSidePB2)):
				if ((self.run1 and self.run3 and self.run4 and self.run5) != True):
					self.run2 = True
								#set relay
					
			else:
				self.run2 = False
				# turn off
							
			#Push Button 3
			if (GPIO.input(LSidePB3) or GPIO.input(RSidePB3)):
				if ((self.run1 and self.run2 and self.run4 and self.run5) != True):
					self.run3 = True
								#set relay
					
			else:
				self.run3 = False
				# turn off	

			#Push Button 4
			if (GPIO.input(LSidePB4) or GPIO.input(RSidePB4)):
				if ((self.run1 and self.run2 and self.run3 and self.run5) != True):
					self.run4 = True
								#set relay
					
			else:
				self.run4 = False
				# turn off
					
			#Push Button 5
			if (GPIO.input(LSidePB5) or GPIO.input(RSidePB5)):
				if ((self.run1 and self.run2 and self.run3 and self.run4) != True):
					self.run5 = True
								#set relay
					
			else:
				self.run5 = False
				# turn off
					

		
			
			if(self.exitProgram == True):
				self.exitProgram = False
				break
            
			# time.sleep(0.2)


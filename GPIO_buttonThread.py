import time
from time import sleep
import datetime
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import RPi.GPIO as GPIO

# Rev B
UpDown = 17
ArmRotate = 27
ArmTelscp = 22
FlrMntLR	= 10
ColRoate = 9
TpHldPBEn = 16
BotHldPBEn = 20

RlyCtrl1 = 11
RlyCtrl2 = 6
RlyCtrl3 = 13
RlyCtrl4 = 19
RlyCtrl5 = 26
RlyCtrl6 = 21

# --------------------------------------------------------------------------------------------------------------
# ----------------------------------- GPIO Control Thread Class ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------   
class GPIO_control(QThread):
	handleButtonSig = pyqtSignal(str) 
    
	def __init__(self):
		QThread.__init__(self)
		
		# GPIO Configuration
		GPIO.setmode(GPIO.BCM)

		# Set input GPIO Pins
		GPIO.setup(FlrMntLR,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(ArmTelscp,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(ArmRotate,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(UpDown,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(ColRoate,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(TpHldPBEn,  	GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(BotHldPBEn,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

		# Set output GPIO Pins
		GPIO.setup(RlyCtrl1,  GPIO.OUT)
		GPIO.setup(RlyCtrl2,  GPIO.OUT)
		GPIO.setup(RlyCtrl3,  GPIO.OUT)
		GPIO.setup(RlyCtrl4,  GPIO.OUT)
		GPIO.setup(RlyCtrl5,  GPIO.OUT)
		GPIO.setup(RlyCtrl6,  GPIO.OUT)

		self.setLow = False
		self.modeSet = "Off"
		self.run1 = False
		self.run2 = False
		self.run3 = False
		self.run4 = False
		self.run5 = False
		self.run6 = False
 	
	def SWpushButton(self, mode):
		self.modeSet = mode

	#Sets all GPIO pins Low
	def	setInitSettings(self):
			GPIO.output(RlyCtrl1, GPIO.LOW)
			GPIO.output(RlyCtrl2, GPIO.LOW)
			GPIO.output(RlyCtrl3, GPIO.LOW)
			GPIO.output(RlyCtrl4, GPIO.HIGH)
			GPIO.output(RlyCtrl5, GPIO.LOW)
			GPIO.output(RlyCtrl6, GPIO.LOW)
			self.handleButtonSig.emit("Off")

	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):

			self.setInitSettings()
				
			# Mode 1 - Left/Right Up and down Push Button 1
			if (GPIO.input(UpDown) or self.modeSet == "Mode 1"):
				if ((self.run2 and self.run3 and self.run4 and self.run5 and self.run6) != True):
					self.run1 = True
					
					#set relay
					GPIO.output(RlyCtrl1, GPIO.HIGH)

					self.handleButtonSig.emit("Mode 1")
			else:
				self.run1 = False
			
			# Mode 2 - Rotate Push Button 2
			if (GPIO.input(ArmRotate) or self.modeSet == "Mode 2"):
				if ((self.run1 and self.run3 and self.run4 and self.run5 and self.run6) != True):
					self.run2 = True

					#set relay
					GPIO.output(RlyCtrl2, GPIO.HIGH)
					self.handleButtonSig.emit("Mode 2")

			else:
				self.run2 = False
							
			# Mode 3 - Arm Telescope button 3
			if (GPIO.input(ArmTelscp) or self.modeSet == "Mode 3"):
				if ((self.run1 and self.run2 and self.run4 and self.run5 and self.run6) != True):
					self.run3 = True

					#set relay
					GPIO.output(RlyCtrl3, GPIO.HIGH)
					self.handleButtonSig.emit("Mode 3")
			else:
				self.run3 = False


		 # Mode 4 - Floor Right <-> Left 4
			if (GPIO.input(FlrMntLR) or self.modeSet == "Mode 4"):
				if ((self.run1 and self.run2 and self.run3 and self.run5 and self.run6) != True):
					self.run4 = True

					
				 	#set relay
					GPIO.output(RlyCtrl4, GPIO.LOW)
					self.handleButtonSig.emit("Mode 4")
			else:
				self.run4 = False
		
			# Mode 5 - Rotate arm column button
			if (GPIO.input(ColRoate)):
				if ((self.run1 and self.run2 and self.run3 and self.run4 and self.run6) != True):
					self.run5 = True

					#set all relay
					GPIO.output(RlyCtrl5, GPIO.HIGH)

			else:
				self.run5 = False

			# Mode 6 - Bottom/Top Handle Push Button - Set All relays
			if (GPIO.input(TpHldPBEn) or GPIO.input(BotHldPBEn) or self.modeSet == "Mode 5"):
				if ((self.run1 and self.run2 and self.run3 and self.run4 and self.run5) != True):
					self.run6 = True
					GPIO.output(RlyCtrl1, GPIO.HIGH)
					GPIO.output(RlyCtrl2, GPIO.HIGH)
					GPIO.output(RlyCtrl3, GPIO.HIGH)
					GPIO.output(RlyCtrl4, GPIO.LOW)
					self.handleButtonSig.emit("Mode 5")

			else:
				self.run6 = False
		
            
			time.sleep(0.2)


import time
from time import sleep
import datetime
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import RPi.GPIO as GPIO

# ~ Rev A
# ~ RSidePB1 = 9
# ~ RSidePB2 = 10
# ~ RSidePB3 = 27
# ~ RSidePB4 = 17
# ~ RSidePB5 = 22
# ~ LSidePB1 = 26
# ~ LSidePB2 = 19
# ~ LSidePB3 = 6
# ~ LSidePB4 = 11
# ~ LSidePB5 = 13

# ~ RlyCtrl1 = 16
# ~ RlyCtrl2 = 12
# ~ RlyCtrl3 = 7
# ~ RlyCtrl4 = 8
# ~ RlyCtrl5 = 25
# ~ RlyCtrl6 = 24
# ~ RlyCtrl7 = 23
# ~ RlyCtrl8 = 18
# ~ RlyCtrl9 = 15
# ~ RlyCtrl10 = 14

# Rev B
FlrMntLR = 17
ArmTelscp = 27
ArmRotate = 22
UpDown	= 10
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
 	
	def SWpushButton(self, mode):
		self.modeSet = mode

	#Sets all GPIO pins Low
	def	setInitSettings(self):
			GPIO.output(RlyCtrl1, GPIO.LOW)
			GPIO.output(RlyCtrl2, GPIO.LOW)
			GPIO.output(RlyCtrl3, GPIO.LOW)
			GPIO.output(RlyCtrl4, GPIO.LOW)
			GPIO.output(RlyCtrl5, GPIO.LOW)
			GPIO.output(RlyCtrl6, GPIO.LOW)
			self.handleButtonSig.emit("Off")


	def run(self):
		self.setPriority(QThread.HighestPriority)

		while (1):

			self.setInitSettings()
				
			# Mode 1 - Left/Right Push Button 1
			# ~ if (GPIO.input(LSidePB4) or GPIO.input(RSidePB1) or self.modeSet == "Mode 2"):
			if (self.modeSet == "Mode 1"):
				if ((self.run2 and self.run3 and self.run4 and self.run5) != True):
					self.run1 = True
					#set relay
					# ~ GPIO.output(RlyCtrl1, GPIO.LOW)
					GPIO.output(RlyCtrl1, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl2, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl3, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl4, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl5, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl6, GPIO.HIGH)

					self.handleButtonSig.emit("Mode 1")
		
			
			# ~ # Mode 2 - Left/Right Push Button 2
			# ~ if (GPIO.input(LSidePB3) or GPIO.input(RSidePB2) or self.modeSet == "Mode 1"):
				# ~ if ((self.run1 and self.run3 and self.run4 and self.run5) != True):
					# ~ self.run2 = True
					# ~ #set relay
					# ~ GPIO.output(RlyCtrl1, GPIO.LOW)
					# ~ self.handleButtonSig.emit("Mode 1")


							
			# ~ # Mode 3 - Left/ Right button 3 and top button
			# ~ if (GPIO.input(LSidePB2) or GPIO.input(RSidePB3) or GPIO.input(RSidePB5)or self.modeSet == "Mode 3"):
				# ~ if ((self.run1 and self.run2 and self.run4 and self.run5) != True):
					# ~ self.run3 = True
					# ~ #set relay
					# ~ GPIO.output(RlyCtrl5, GPIO.HIGH)
					# ~ self.handleButtonSig.emit("Mode 3")


			# ~ else:
				# ~ self.run3 = False


		 # ~ # Mode 4 
			# ~ if (GPIO.input(LSidePB1) or GPIO.input(RSidePB4) or self.modeSet == "Mode 4"):
				# ~ if ((self.run1 and self.run2 and self.run3 and self.run5) != True):
					# ~ self.run4 = True
				 	# ~ #set relay
					# ~ # GPIO.output(RlyCtrl6, GPIO.HIGH)
					# ~ self.handleButtonSig.emit("Mode 4")

					
			# ~ else:
				# ~ self.run4 = False
		
	
			# ~ # Mode 5 - Bottom Push Button - Set All relays
			# ~ if (GPIO.input(LSidePB5) or self.modeSet == "Mode 5"):
				# ~ if ((self.run1 and self.run2 and self.run3 and self.run4) != True):
					# ~ self.run5 = True
					# ~ #set all relay
					# ~ GPIO.output(RlyCtrl1, GPIO.LOW)
					# ~ GPIO.output(RlyCtrl3, GPIO.HIGH)
					# ~ GPIO.output(RlyCtrl5, GPIO.HIGH)
					# ~ self.handleButtonSig.emit("Mode 5")

			# ~ else:
				# ~ self.run5 = False
		
		
			# ~ if (self.modeSet == "Mode 1"):
				# ~ print ("HI")
				# ~ GPIO.output(RlyCtrl1, GPIO.HIGH)
				# ~ GPIO.output(RlyCtrl2, GPIO.HIGH)
				# ~ GPIO.output(RlyCtrl3, GPIO.HIGH)
				
			# ~ print("col: " + str(GPIO.input(ColRoate)))
			# ~ print("flR: " + str(GPIO.input(FlrMntLR)))
			# ~ print("updo: " + str(GPIO.input(UpDown)))
			# ~ print("armtel: " + str(GPIO.input(ArmTelscp)))
			# ~ print("armRotate: " + str(GPIO.input(ArmRotate)))
			# ~ print("armRotate: " + str(GPIO.input(TpHldPBEn)))
			# ~ print("armRotate: " + str(GPIO.input(BotHldPBEn)))
			# ~ print(GPIO.input(RSidePB1))
			# ~ print(GPIO.input(RSidePB2))
			# ~ print(GPIO.input(RSidePB3))
			# ~ print(GPIO.input(RSidePB4))
			# ~ print(GPIO.input(RSidePB5))
            
			time.sleep(0.2)


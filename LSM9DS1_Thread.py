import time
from pylsm9ds1 import ACC_GYRO
from pylsm9ds1 import MAG
from pylsm9ds1 import SMBusDriver
from time import sleep
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

             
# --------------------------------------------------------------------------------------------------------------
# ----------------------------- LSM9DS1 Accelerometer Thread Class -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------                   
class AcellerometerThread(QThread):
	axisSignals = pyqtSignal(int, int, int) 
    
	def __init__(self):
		QThread.__init__(self)
		self.exitProgram = False
		
		# I2C connection:
		acc_driver = SMBusDriver(ACC_GYRO.ADDRESS, 3)
		mag_driver = SMBusDriver(MAG.ADDRESS, 3)
		self.imu = ACC_GYRO(acc_driver)
		self.mag = MAG(mag_driver)
		
		if self.imu.selfTest() is True:
			self.imu.enableGyro()
			self.imu.enableAcc()
			# ~ self.mag.enable()
		
    #Sets up the program to exit when the main window is shutting down
	def Set_Exit_Program(self, exiter):
		self.exitProgram = exiter,
        
	def run(self):

		while (1):
			gx, gy, gz = self.imu.readGyro()
			# ~ mx, my, mz = self.mag.read()
			# ~ temp = self.imu.readTemp()
			ax, ay, az = self.imu.readAcc()
			# ~ print ("Accel: " + str(ax) + ", " + str(ay) + ", " + str(az) )

	  
			self.axisSignals.emit(ax,ay,az)
			
			if(self.exitProgram == True):
				self.exitProgram = False
				break
            
			time.sleep(0.1)
          
				
            

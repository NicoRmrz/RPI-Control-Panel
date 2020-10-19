import time
from pylsm9ds1 import ACC_GYRO
from pylsm9ds1 import MAG
from pylsm9ds1 import SMBusDriver
from time import sleep
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

gxlist = []
gylist = []
gzlist = []
axlist = []
aylist = []
azlist = []

SAMPLESIZE = 20 

DPS = 0.07
     
# --------------------------------------------------------------------------------------------------------------
# ----------------------------- LSM9DS1 Accelerometer Thread Class -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------                   
class AcellerometerThread(QThread):
	axisSignals = pyqtSignal(int, int, int) 
	gyroSignals = pyqtSignal(int, int, int) 
    
	def __init__(self):
		QThread.__init__(self)
		self.gxAvg = 0
		self.gyAvg = 0
		self.gzAvg = 0
		self.axAvg = 0
		self.ayAvg = 0
		self.azAvg = 0
		
		# I2C connection:
		acc_driver = SMBusDriver(ACC_GYRO.ADDRESS, 4)
		mag_driver = SMBusDriver(MAG.ADDRESS, 4)
		self.imu = ACC_GYRO(acc_driver)
		self.mag = MAG(mag_driver)
		
		if self.imu.selfTest() is True:
			self.imu.enableGyro()
			self.imu.enableAcc()
			# ~ self.mag.enable()
        
	def Average(self, lst):
		return sum(lst) / len (lst)
		
	def configMeasurement(self, x, y):
		finalMeas = x
		if (x < 0 and y > 0):
			y = -1 * y
			finalMeas = -90 + y
			
		if (x > 0 and y > 0):
			finalMeas = 90 + y
			
		return finalMeas
        
	def run(self):

		while (1):
			gx, gy, gz = self.imu.readGyro()
			ax, ay, az = self.imu.readAcc()

			# Smooth ax
			if len(axlist) < SAMPLESIZE:
				axlist.append(ax)
			else:
				self.axAvg = self.Average(axlist)
				axlist.clear()

			# Smooth ay
			if len(aylist) < SAMPLESIZE:
				aylist.append(ay)
			else:
				self.ayAvg = self.Average(aylist)
				aylist.clear()

			# Smooth az
			if len(azlist) < SAMPLESIZE:
				azlist.append(az)
			else:
				self.azAvg = self.Average(azlist)
				azlist.clear()

			updated_x = self.axAvg * DPS
			updated_y = self.ayAvg * DPS
			updated_z = self.azAvg * DPS
			
			# fix readings over 90 deg 
			calibratedMeas = self.configMeasurement(self.axAvg * DPS, self.ayAvg * DPS) 

			# Smoothed all readings with DPS
			self.axisSignals.emit(calibratedMeas, updated_y, self.azAvg * DPS)
		
			time.sleep(0.01)
          


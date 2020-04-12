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

SAMPLESIZE = 4 

# ~ DPS = 0.00875 # for degrees/second values
# ~ DPS = 1
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
        
	def run(self):

		while (1):
			gx, gy, gz = self.imu.readGyro()
			# ~ mx, my, mz = self.mag.read()
			# ~ temp = self.imu.readTemp()
			ax, ay, az = self.imu.readAcc()

			# # Smooth gx
			# if len(gxlist) < SAMPLESIZE:
			# 	gxlist.append(gx)
			# else:
			# 	self.gxAvg = self.Average(gxlist)
			# 	gxlist.clear()

			# # Smooth gy
			# if len(gylist) < SAMPLESIZE:
			# 	gylist.append(gy)
			# else:
			# 	self.gyAvg = self.Average(gylist)
			# 	gylist.clear()

			# # Smooth gz
			# if len(gzlist) < SAMPLESIZE:
			# 	gzlist.append(gz)
			# else:
			# 	self.gzAvg = self.Average(gzlist)
			# 	gzlist.clear()

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
			updated_x = updated_x
			
			# Smoothed all readings with DPS
			# ~ self.gyroSignals.emit(self.gxAvg * DPS, self.gyAvg * DPS, self.gzAvg * DPS)
			self.axisSignals.emit(updated_x, self.ayAvg * DPS, self.azAvg * DPS)
			# ~ print("X " + str(self.axAvg * DPS) +", Y "+ str(self.ayAvg * DPS))

			# Smoothed readings only
			# ~ self.gyroSignals.emit(self.gxAvg , self.gyAvg , self.gzAvg )
			# ~ self.axisSignals.emit(self.axAvg , self.ayAvg , self.azAvg )

			# Raw readings with DPS
			# self.gyroSignals.emit(gx * DPS,gy * DPS,gz * DPS)
			# self.axisSignals.emit(ay * DPS, ay * DPS,az * DPS)

			# Raw readings
			# ~ self.gyroSignals.emit(gx,gy,gz)
			# ~ self.axisSignals.emit(ax,ay,az)

            
			time.sleep(0.1)
          
				
            

# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mainWindow import Ui_MainWindow

from PyQt5 import QtWidgets

from PyQt5.QtGui import QPixmap, QIcon
from threading import Event

#imports from user made file
from newValue import Controller,  ControlArduino    
# from GPIO_buttonThread import GPIO_control
# import RPi.GPIO as GPIO
# from LSM9DS1_Thread import AcellerometerThread
# from ADS79241_Thread import ADC_thread


# Icon Image locations
Main_path = os.getcwd() + "/"
Icon_Path = Main_path + "/icons/logo.png"
Mediatech_Path = Main_path + "/icons/Medicatech.png"
        
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        


        self.setWindowIcon(QIcon(Icon_Path))
        
        # self.MediLogo.rotate(180)

        self.rotateGUI(0)

        self.stop_flag_time =  Event()
        self.stop_flag_RS232 =  Event()

        self.getController = Controller(self.stop_flag_time)
        self.getController.start()
        self.getController.newTime.connect(self.updateTime)
 
        self.getArduino = ControlArduino(self.stop_flag_RS232)
        self.getArduino.newValue.connect(self.updatePoti)  
        self.getArduino.testRS232.connect(self.updateInfoRS232)          
        self.getArduino.start() 


        # self.GPIOthread = GPIO_control()
        # self.GPIOthread.start()

        # self.GPIOthread.setAllLow(True)

        # ~ self.accelerometer = AcellerometerThread()
        # ~ self.accelerometer.start() 
        # ~ self.accelerometer.axisSignals.connect(self.updateAccelerometer)

        # ~ self.ADC = ADC_thread()
        # ~ self.ADC.start() 

        self.btnExit.clicked.connect(self.on_btnExit_clicked)

        self.leftButton1.pressed.connect(self.leftButton1_Clicked)
        self.leftButton2.pressed.connect(self.leftButton2_Clicked)
        self.leftButton3.pressed.connect(self.leftButton3_Clicked)
        self.leftButton4.pressed.connect(self.leftButton4_Clicked)

        self.rightButton1.pressed.connect(self.rightButton1_Clicked)
        self.rightButton2.pressed.connect(self.rightButton2_Clicked)
        self.rightButton3.pressed.connect(self.rightButton3_Clicked)
        self.rightButton4.pressed.connect(self.rightButton4_Clicked)


        
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.stop_flag_time.set()
        self.stop_flag_RS232.set()
        # self.GPIOthread.Set_Exit_Program(True)
        # self.ADC.Set_Exit_Program(True)
        # GPIO.cleanup()
        sys.exit(0);

    def updateTime(self,  timeInterval):
        self.clockTime.setText("Time:  " + timeInterval)

    def updatePoti(self, poti,  poti2, poti3):
        self.SID1_Data.setText(str(poti) + " in")
        self.SID2_Data.setText(str(poti2) + " in")
        self.SID3_Data.setText(str(poti3) + " in")
        
    def updateInfoRS232(self, rs232):
        print(rs232)
        if rs232:
            self.lblRSinfo.setText("MCU Connected")
        else:
            self.lblRSinfo.setText("MCU Connection Failed")
            self.SID1_Data.setText("Error")
            self.SID2_Data.setText("Error")
            self.SID3_Data.setText("Error")
            self.stop_flag_RS232.set()

    def updateAccelerometer(self, x, y, z):
        self.xAxis.setText("X: " + str(x))
        self.yAxis.setText("Y: " + str(y))
        self.zAxis.setText("Z: " + str(z))


    def rotateGUI(self, degree):
        self.MediLogo.rotate(degree)
        self.timeView.rotate(degree)

        self.exitBtn_View.rotate(degree)
        self.LBtn1_View.rotate(degree)
        self.LBtn2_View.rotate(degree)
        self.LBtn3_View.rotate(degree)
        self.LBtn4_View.rotate(degree)        
        self.RBtn1_View.rotate(degree)
        self.RBtn2_View.rotate(degree)
        self.RBtn3_View.rotate(degree)
        self.RBtn4_View.rotate(degree)

        self.SID1Label_View.rotate(degree)
        self.SID2Label_View.rotate(degree)
        self.SID3Label_View.rotate(degree)

        self.SID1Data_View.rotate(degree)
        self.SID2Data_View.rotate(degree)
        self.SID3Data_View.rotate(degree)
        self.xAx_View.rotate(degree)
        self.yAx_View.rotate(degree)
        self.zAx_View.rotate(degree)



    def leftButton1_Clicked(self):
        print("Left Button 1 Pressed!")
    def leftButton2_Clicked(self):
        print("Left Button 2 Pressed!")
    def leftButton3_Clicked(self):
        print("Left Button 3 Pressed!")
    def leftButton4_Clicked(self):
        print("Left Button 4 Pressed!")

    def rightButton1_Clicked(self):
        print("Right Button 1 Pressed!")
    def rightButton2_Clicked(self):
        print("Right Button 2 Pressed!")
    def rightButton3_Clicked(self):
        print("Right Button 3 Pressed!")
    def rightButton4_Clicked(self):
        print("Right Button 4 Pressed!")

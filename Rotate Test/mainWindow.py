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
        
        scene = QtWidgets.QGraphicsScene()

        
        scene.addPixmap(QPixmap(Mediatech_Path))
        # scene.addWidget(self.lblAnzeige)
        # scene.addWidget(self.label_4)
        # scene.addWidget(self.Hlayout)
        self.setWindowIcon(QIcon(Icon_Path))
        
        self.MediLogo.setScene(scene)
        self.MediLogo.rotate(180)


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


        
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.stop_flag_time.set()
        self.stop_flag_RS232.set()
        self.GPIOthread.Set_Exit_Program(True)
        self.ADC.Set_Exit_Program(True)
        GPIO.cleanup()
        sys.exit(0);

    def updateTime(self,  timeInterval):
        self.lbltime.setText("Time:  " + timeInterval)

    def updatePoti(self, poti,  poti2, poti3):
        self.lblAnzeige.setText(str(poti) + " in")
        self.lblAnzeige2.setText(str(poti2) + " in")
        self.lblAnzeige3.setText(str(poti3) + " in")
        
    def updateInfoRS232(self, rs232):
        print(rs232)
        if rs232:
            self.lblRSinfo.setText("MCU Connected")
        else:
            self.lblRSinfo.setText("MCU Connection Failed")
            self.lblAnzeige.setText("Error")
            self.lblAnzeige2.setText("Error")
            self.lblAnzeige3.setText("Error")
            self.stop_flag_RS232.set()

    def updateAccelerometer(self, x, y, z):
        self.xAxis.setText("X: " + str(x))
        self.yAxis.setText("Y: " + str(y))
        self.zAxis.setText("Z: " + str(z))


    def rotateGUI(self, degree):
        self.MediLogo.rotate(180)
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
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()

# Icon Image locations
Main_path = os.getcwd() + "/"
Icon_Path = Main_path + "/icons/logo.png"
Mediatech_Path = Main_path + "/icons/Medicatech.png"
Down_Idle = Main_path + "/icons/down_grey.png"
Down_Pressed = Main_path + "/icons/down_grey_pressed.png"
Up_Idle = Main_path + "/icons/up_grey.png"
Up_Pressed = Main_path + "/icons/up_grey_pressed.png"
Rotate_Idle = Main_path + "/icons/rotation.png"
Rotate_Pressed = Main_path + "/icons/rotation_pressed.png"
Left_Idle = Main_path + "/icons/left_grey.png"
Left_Pressed = Main_path + "/icons/left_grey_pressed.png"
Right_Idle = Main_path + "/icons/right_grey.png"
Right_Pressed = Main_path + "/icons/right_grey_pressed.png"
        
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowIcon(QIcon(Icon_Path))
        
        self.rotateGUI(0)

        self.stop_flag_time =  Event()
        self.stop_flag_RS232 =  Event()

        self.getController = Controller(self.stop_flag_time)
        self.getController.start()
        self.getController.newTime.connect(self.updateTime)
 
        # self.getArduino = ControlArduino(self.stop_flag_RS232)
        # self.getArduino.newValue.connect(self.updatePoti)  
        # self.getArduino.testRS232.connect(self.updateInfoRS232)          
        # self.getArduino.start() 


        # self.GPIOthread = GPIO_control()
        # self.GPIOthread.start()
        # self.GPIOthread.setInitSettings()
        # self.GPIOthread.handleButtonSig.connect(self.buttonHandlers)

        # ~ self.accelerometer = AcellerometerThread()
        # ~ self.accelerometer.start() 
        # ~ self.accelerometer.axisSignals.connect(self.updateAccelerometer)

        # ~ self.ADC = ADC_thread()
        # ~ self.ADC.start() 
        # ~ self.ADC.ADC_meas.connect(self.updateSID)

        self.btnExit.clicked.connect(self.on_btnExit_clicked)

        self.leftButton1.pressed.connect(self.leftButton1_Clicked)
        self.leftButton1.released.connect(self.leftButton1_Released)

        self.leftButton2.pressed.connect(self.leftButton2_Clicked)
        self.leftButton2.released.connect(self.leftButton2_Released)

        self.leftButton3.pressed.connect(self.leftButton3_Clicked)
        self.leftButton3.released.connect(self.leftButton3_Released)

        self.leftButton4.pressed.connect(self.leftButton4_Clicked)
        self.leftButton4.released.connect(self.leftButton4_Released)

        self.rightButton1.pressed.connect(self.rightButton1_Clicked)
        self.rightButton1.released.connect(self.rightButton1_Released)

        self.rightButton2.pressed.connect(self.rightButton2_Clicked)
        self.rightButton2.released.connect(self.rightButton2_Released)

        self.rightButton3.pressed.connect(self.rightButton3_Clicked)
        self.rightButton3.released.connect(self.rightButton3_Released)

        self.rightButton4.pressed.connect(self.rightButton4_Clicked)
        self.rightButton4.released.connect(self.rightButton4_Released)


        
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.stop_flag_time.set()
        # self.stop_flag_RS232.set()
        # self.GPIOthread.Set_Exit_Program(True)
        # self.ADC.Set_Exit_Program(True)
        # GPIO.cleanup()
        sys.exit(0);

    def updateTime(self,  timeInterval):
        self.clockTime.setText("Time:  " + timeInterval)

    def updateSID(self, poti,  poti2, poti3):
        self.SID1_Data.setText(str(poti) + " in")
        self.SID2_Data.setText(str(poti2) + " in")
        self.SID3_Data.setText(str(poti3) + " in")
        
    # def updateInfoRS232(self, rs232):
    #     print(rs232)
    #     if rs232:
    #         self.lblRSinfo.setText("MCU Connected")
    #     else:
    #         self.lblRSinfo.setText("MCU Connection Failed")
    #         self.SID1_Data.setText("Error")
    #         self.SID2_Data.setText("Error")
    #         self.SID3_Data.setText("Error")
            # self.stop_flag_RS232.set()

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

    def buttonHandlers(self, mode):
        if mode == "Off":
            self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton1.setIcon(QIcon(Rotate_Idle))
            self.rightButton1.setIcon(QIcon(Rotate_Idle))
            self.leftButton2.setIcon(QIcon(Left_Idle))
            self.rightButton2.setIcon(QIcon(Right_Idle))
            self.leftButton3.setIcon(QIcon(Up_Idle))
            self.rightButton3.setIcon(QIcon(Down_Idle))

        if mode == "Mode 1":
            self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton1.setStyleSheet(GUI_Style.buttonPressed) 
            self.leftButton1.setIcon(QIcon(Rotate_Pressed))
            self.rightButton1.setIcon(QIcon(Rotate_Pressed))       
        if mode == "Mode 2":
            self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)    
            self.leftButton2.setIcon(QIcon(Left_Pressed))
            self.rightButton2.setIcon(QIcon(Right_Pressed))
        if mode == "Mode 3":
            self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.leftButton3.setIcon(QIcon(Up_Pressed))
            self.rightButton3.setIcon(QIcon(Down_Pressed))
        if mode == "Mode 4":
            self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
            self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
        if mode == "Mode 5":
            self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton1.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonPressed) 
            self.leftButton1.setIcon(QIcon(Rotate_Pressed))
            self.rightButton1.setIcon(QIcon(Rotate_Pressed)) 
            self.leftButton2.setIcon(QIcon(Left_Pressed))
            self.rightButton2.setIcon(QIcon(Right_Pressed))
            self.leftButton3.setIcon(QIcon(Up_Pressed))
            self.rightButton3.setIcon(QIcon(Down_Pressed))

    def leftButton1_Clicked(self):
        self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton1.setStyleSheet(GUI_Style.buttonPressed)        
        self.leftButton1.setIcon(QIcon(Rotate_Pressed))
        self.rightButton1.setIcon(QIcon(Rotate_Pressed))
        # self.GPIOthread.SWpushButton("Mode 1")

    def leftButton1_Released(self):
        self.leftButton1.setIcon(QIcon(Rotate_Idle))
        self.rightButton1.setIcon(QIcon(Rotate_Idle))
        self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)        
        # self.GPIOthread.SWpushButton("Off")
        
    def leftButton2_Clicked(self):
        self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton2.setIcon(QIcon(Left_Pressed))
        self.rightButton2.setIcon(QIcon(Right_Pressed))
        # self.GPIOthread.SWpushButton("Mode 2")

    def leftButton2_Released(self):
        self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setIcon(QIcon(Left_Idle))
        self.rightButton2.setIcon(QIcon(Right_Idle))
        # self.GPIOthread.SWpushButton("Off")

    def leftButton3_Clicked(self):
        self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton3.setIcon(QIcon(Up_Pressed))
        self.rightButton3.setIcon(QIcon(Down_Pressed))
        # self.GPIOthread.SWpushButton("Mode 3")

    def leftButton3_Released(self):
        self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setIcon(QIcon(Up_Idle))
        self.rightButton3.setIcon(QIcon(Down_Idle))
        # self.GPIOthread.SWpushButton("Off")

    def leftButton4_Clicked(self):
        self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
        # self.GPIOthread.SWpushButton("Mode 4")


    def leftButton4_Released(self):
        self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)
        # self.GPIOthread.SWpushButton("Off")

    def rightButton1_Clicked(self):
        self.rightButton1.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton1.setIcon(QIcon(Rotate_Pressed))
        self.rightButton1.setIcon(QIcon(Rotate_Pressed))
        # self.GPIOthread.SWpushButton("Mode 1")

    def rightButton1_Released(self):
        self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton1.setIcon(QIcon(Rotate_Idle))
        self.rightButton1.setIcon(QIcon(Rotate_Idle))
        # self.GPIOthread.SWpushButton("Off")

    def rightButton2_Clicked(self):
        self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton2.setIcon(QIcon(Left_Pressed))
        self.rightButton2.setIcon(QIcon(Right_Pressed))
        # self.GPIOthread.SWpushButton("Mode 2")


    def rightButton2_Released(self):
        self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setIcon(QIcon(Left_Idle))
        self.rightButton2.setIcon(QIcon(Right_Idle))
        # self.GPIOthread.SWpushButton("Off")

    def rightButton3_Clicked(self):
        self.rightButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton3.setIcon(QIcon(Up_Pressed))
        self.rightButton3.setIcon(QIcon(Down_Pressed))
        # self.GPIOthread.SWpushButton("Mode 3")

    def rightButton3_Released(self):
        self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setIcon(QIcon(Up_Idle))
        self.rightButton3.setIcon(QIcon(Down_Idle))       
        # self.GPIOthread.SWpushButton("Off")

    def rightButton4_Clicked(self):
        self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
        # self.GPIOthread.SWpushButton("Mode 4")


    def rightButton4_Released(self):
        self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)
        # self.GPIOthread.SWpushButton("Off")

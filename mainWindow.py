# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QIcon
from threading import Event
import RPi.GPIO as GPIO

#imports from user made file
from Ui_mainWindow import Ui_MainWindow
from timeValue import Controller    
from GPIO_buttonThread import GPIO_control
from LSM9DS1_Thread import AcellerometerThread
from ADS1115_Thread import ADC_thread
from GUI_Stylesheets import GUI_Stylesheets
from angleMeasGraphic import angleGraphic

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
Rotate1_Idle = Main_path + "/icons/rotation1.png"
Rotate1_Pressed = Main_path + "/icons/rotation1_pressed.png"
Left_Idle = Main_path + "/icons/left_grey.png"
Left_Pressed = Main_path + "/icons/left_grey_pressed.png"
Right_Idle = Main_path + "/icons/right_grey.png"
Right_Pressed = Main_path + "/icons/right_grey_pressed.png"
Telescope_Idle = Main_path + "/icons/Telescope_Idle.png"
Telescope1_Idle = Main_path + "/icons/Telescope1_Idle.png"
Telescope_Pressed = Main_path + "/icons/Telescope_Pressed.png"
Telescope1_Pressed = Main_path + "/icons/Telescope1_Pressed.png"
UpDown_Idle = Main_path + "/icons/UpDown_Idle.png"
UpDown_Pressed = Main_path + "/icons/UpDown_Pressed.png"
LeftRight_Idle = Main_path + "/icons/LeftRight_Idle.png" 
LeftRight_Pressed = Main_path + "/icons/LeftRight_Pressed.png"

ROTATE_RIGHT = 65
ROTATE_LEFT = -65

RESET_RIGHT = -90
RESET_LEFT = 90
DEFAULT_POS = 0

DEFAULT_SIZE = 325
SIDE_SIZE = 120

# IDLE
LEFT1_ICON = UpDown_Idle
LEFT2_ICON = Rotate_Idle
LEFT3_ICON = Telescope_Idle
LEFT4_ICON = LeftRight_Idle
RIGHT1_ICON = UpDown_Idle
RIGHT2_ICON = Rotate1_Idle
RIGHT3_ICON = Telescope_Idle
RIGHT4_ICON = LeftRight_Idle

# PRESSED
LEFT1_ICON_PRES = UpDown_Pressed
LEFT2_ICON_PRES = Rotate_Pressed
LEFT3_ICON_PRES = Telescope_Pressed
LEFT4_ICON_PRES = LeftRight_Pressed
RIGHT1_ICON_PRES = UpDown_Pressed
RIGHT2_ICON_PRES = Rotate1_Pressed
RIGHT3_ICON_PRES = Telescope_Pressed
RIGHT4_ICON_PRES = LeftRight_Pressed

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowIcon(QIcon(Icon_Path))
        self.prevOrientation = "Normal"

        self.stop_flag_time =  Event()
        self.getController = Controller(self.stop_flag_time)
        self.getController.start()
        self.getController.newTime.connect(self.updateTime)

        self.GPIOthread = GPIO_control()
        self.GPIOthread.start()
        self.GPIOthread.setInitSettings()
        self.GPIOthread.handleButtonSig.connect(self.buttonHandlers)

        self.accelerometer = AcellerometerThread()
        self.accelerometer.start() 
        self.accelerometer.axisSignals.connect(self.updateAccelerometer)
        # ~ self.accelerometer.gyroSignals.connect(self.updateGyroscope)

        self.ADC = ADC_thread()
        self.ADC.start() 
        self.ADC.ADC_meas.connect(self.updateSID)

        self.angleImg = angleGraphic()
        self.angleImg.setScreenOrientation(self.prevOrientation)
        self.angleImg.setAngleTick(DEFAULT_POS)
        self.rotateGUI(DEFAULT_POS)

        self.AcelLayout.addWidget(self.angleImg)
        self.AcelLayout.addWidget(self.xAx_View, 0,Qt.AlignCenter)

        # connect signals to slots
        self.btnExit.clicked.connect(self.on_btnExit_clicked)

        self.leftButton1.pressed.connect(self.Button1_Clicked)
        self.rightButton1.pressed.connect(self.Button1_Clicked)
        self.leftButton1.released.connect(self.Button1_Released)
        self.rightButton1.released.connect(self.Button1_Released)

        self.leftButton2.pressed.connect(self.Button2_Clicked)
        self.rightButton2.pressed.connect(self.Button2_Clicked)
        self.leftButton2.released.connect(self.Button2_Released)
        self.rightButton2.released.connect(self.Button2_Released)

        self.leftButton3.pressed.connect(self.Button3_Clicked)
        self.rightButton3.pressed.connect(self.Button3_Clicked)
        self.leftButton3.released.connect(self.Button3_Released)
        self.rightButton3.released.connect(self.Button3_Released)

        self.leftButton4.pressed.connect(self.Button4_Clicked)
        self.rightButton4.pressed.connect(self.Button4_Clicked)
        self.leftButton4.released.connect(self.Button4_Released)
        self.rightButton4.released.connect(self.Button4_Released)

        
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.stop_flag_time.set()
        self.GPIOthread.terminate()
        self.GPIOthread.wait(100)        
        self.ADC.terminate()
        self.ADC.wait(100)        
        self.accelerometer.terminate()
        self.accelerometer.wait(100)        
        GPIO.cleanup()
        sys.exit(0);

    def updateTime(self,  timeInterval):
        self.clockTime.setText("Time:  " + timeInterval)

    def updateSID(self, floorSensor, verticalSensor):
        # ~ self.SID1_Data.setText(str(floorSensor) + " mm")
        # ~ self.SID2_Data.setText(str(verticalSensor) + " mm")        
        self.SID1_Data.setText(str(floorSensor) + " in")
        self.SID2_Data.setText(str(verticalSensor) + " in")        

    def updateAccelerometer(self, x, y, z):
        self.xAxis.setText(str(x) + " \N{DEGREE SIGN}")
        # ~ print("x: " + str(x) + " y: " + str(y) + " z: " + str(z))

        # For Screen Rotation
        self.rotateGUI(-1*x)

        # Set Angle tick rotation value
        self.angleImg.setAngleTick((-1*x)/2)

    def updateGyroscope(self, x, y, z):
        self.xGyro.setText("X: " + str(x))
        self.yGyro.setText("Y: " + str(y))
        self.zGyro.setText("Z: " + str(z))

    def rotateObjects(self, degree):
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
        self.SID1img.rotate(degree)
        self.SID2img.rotate(degree)
        self.SID1Data_View.rotate(degree)
        self.SID2Data_View.rotate(degree)
        self.xAx_View.rotate(degree)
        self.yAx_View.rotate(degree)
        self.zAx_View.rotate(degree)


    def rotateGUI(self, degree):

        # Greater than 80 degrees for Right orientation
        if (degree >= ROTATE_RIGHT and self.prevOrientation!="Right"):
            self.rotateObjects(RESET_LEFT)
            self.prevOrientation = "Right"
            self.angleImg.setScreenOrientation(self.prevOrientation)

        	# --- Layout Clockwise view ---
        	# Remove Widget from normal view
            self.HeaderLayout.removeWidget(self.MediLogo)
            self.HeaderLayout.removeWidget(self.timeView)
            self.HeaderLayout.removeWidget(self.exitBtn_View)

            # Layout New Header
            self.rightLogoLayout.addWidget(self.MediLogo, 1, Qt.AlignTop)
            self.MediLogo.setMinimumSize(QtCore.QSize(50, 400))
            self.rightHeaderLayout.addWidget(self.timeView, 1, Qt.AlignBottom)
            self.rightHeaderLayout.addWidget(self.exitBtn_View, 1, Qt.AlignBottom)

            # Relayout center objects
            # First remove
            # self.SID1Layout.removeWidget(self.SID1img)
            # self.SID1Layout.removeWidget(self.SID1Data_View)
            # self.SID2Layout.removeWidget(self.SID2img)
            # self.SID2Layout.removeWidget(self.SID2Data_View)
            self.AcelLayout.removeWidget(self.angleImg)
            self.AcelLayout.removeWidget(self.xAx_View)

            # Then layout
            # self.SID1img.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # self.SID2img.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # ~ self.angleImg.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # ~ self.angleImg.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # self.SID1Layout.addWidget(self.SID1img)
            # self.SID1Layout.addWidget(self.SID1Data_View, 1, Qt.AlignTop)            
            # self.SID2Layout.addWidget(self.SID2img)
            # self.SID2Layout.addWidget(self.SID2Data_View, 1, Qt.AlignTop)
            self.AcelLayout.addWidget(self.angleImg)
            self.AcelLayout.addWidget(self.xAx_View)
            

            # Align center objects
            # self.SID1Layout.setSpacing(50)
            # self.SID1Layout.setContentsMargins(0, 75, 0, 0)
            # self.SID2Layout.setSpacing(50)
            # self.SID2Layout.setContentsMargins(0, 75, 0, 0)
            self.AcelLayout.setSpacing(0)
            self.AcelLayout.setContentsMargins(0, 0, 0, 0)

        # Less than -80 degrees for Left orientation
        elif  (degree <= ROTATE_LEFT and self.prevOrientation!="Left"):
            self.rotateObjects(RESET_RIGHT)
            self.prevOrientation = "Left"
            self.angleImg.setScreenOrientation(self.prevOrientation)

            # --- Layout CounterClockwise view ---
			# Remove Widget from normal view
            self.HeaderLayout.removeWidget(self.MediLogo)
            self.HeaderLayout.removeWidget(self.timeView)
            self.HeaderLayout.removeWidget(self.exitBtn_View)

            # Layout New Header            
            self.leftLogoLayout.addWidget(self.MediLogo, 1, Qt.AlignBottom)
            self.MediLogo.setMinimumSize(QtCore.QSize(45, 400))
            self.leftHeaderLayout.addWidget(self.exitBtn_View, 1, Qt.AlignTop)
            self.leftHeaderLayout.addWidget(self.timeView, 1,Qt.AlignTop)

  			# Relayout center objects
            # First remove
            # self.SID1Layout.removeWidget(self.SID1img)
            # self.SID1Layout.removeWidget(self.SID1Data_View)
            # self.SID2Layout.removeWidget(self.SID2img)
            # self.SID2Layout.removeWidget(self.SID2Data_View)
            self.AcelLayout.removeWidget(self.angleImg)
            self.AcelLayout.removeWidget(self.xAx_View)

            # Then layout
            # self.SID1img.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # self.SID2img.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # ~ self.angleImg.setMaximumSize(QtCore.QSize(SIDE_SIZE, SIDE_SIZE))
            # self.SID1Layout.addWidget(self.SID1Data_View, 1, Qt.AlignBottom)       
            # self.SID1Layout.addWidget(self.SID1img)
            # self.SID2Layout.addWidget(self.SID2Data_View, 1, Qt.AlignBottom)
            # self.SID2Layout.addWidget(self.SID2img)
            # self.AcelLayout.addWidget(self.xAx_View)
            self.AcelLayout.addWidget(self.angleImg)
            self.AcelLayout.addWidget(self.xAx_View)

            # Align center objects
            # self.SID1Layout.setSpacing(50)
            # self.SID1Layout.setContentsMargins(0, 0, 0, 75)
            # self.SID2Layout.setSpacing(50)
            # self.SID2Layout.setContentsMargins(0, 0, 0, 75)
            self.AcelLayout.setSpacing(0)
            self.AcelLayout.setContentsMargins(0, 0, 0, 0)

        # Default orientation 0 degrees +/-80
        elif (degree > ROTATE_LEFT and degree < ROTATE_RIGHT and self.prevOrientation!="Normal"):
            self.rotateObjects(DEFAULT_POS)
            self.prevOrientation ="Normal"
            self.angleImg.setScreenOrientation(self.prevOrientation)

        	# check which orientation the screen currently is
            if (self.rightHeaderLayout.count() > 1):
                self.rotateObjects(RESET_RIGHT)

                self.rightLogoLayout.removeWidget(self.MediLogo)
                self.rightHeaderLayout.removeWidget(self.timeView)
                self.rightHeaderLayout.removeWidget(self.exitBtn_View)

            if (self.leftHeaderLayout.count() > 1):
                self.rotateObjects(RESET_LEFT)

                self.leftLogoLayout.removeWidget(self.MediLogo)
                self.leftHeaderLayout.removeWidget(self.timeView)
                self.leftHeaderLayout.removeWidget(self.exitBtn_View)

            # Relayout center objects
            # First remove
            # self.SID1Layout.removeWidget(self.SID1img)
            # self.SID1Layout.removeWidget(self.SID1Data_View)
            # self.SID2Layout.removeWidget(self.SID2img)
            # self.SID2Layout.removeWidget(self.SID2Data_View)
            self.AcelLayout.removeWidget(self.angleImg)
            self.AcelLayout.removeWidget(self.xAx_View)

            # self.SID1Layout.addWidget(self.SID1img)
            # self.SID1Layout.addWidget(self.SID1Data_View, 1, Qt.AlignTop)
            # self.SID2Layout.addWidget(self.SID2img)
            self.AcelLayout.addWidget(self.angleImg)
            self.AcelLayout.addWidget(self.xAx_View, 0, Qt.AlignCenter)
            # self.SID2Layout.addWidget(self.SID2Data_View, 1, Qt.AlignTop)

            # Add widgets to layout
            self.HeaderLayout.addWidget(self.MediLogo, Qt.AlignLeft)
            self.HeaderLayout.addWidget(self.timeView, Qt.AlignRight)
            self.HeaderLayout.addWidget(self.exitBtn_View)

            # Restore mediatech logo size
            self.MediLogo.setMinimumSize(QtCore.QSize(378, 78))
            self.MediLogo.setMaximumSize(QtCore.QSize(759, 159))

            # Restore center objects
            # self.SID1img.setMaximumSize(QtCore.QSize(DEFAULT_SIZE, DEFAULT_SIZE))
            # self.SID2img.setMaximumSize(QtCore.QSize(DEFAULT_SIZE, DEFAULT_SIZE))
            self.angleImg.setMaximumSize(QtCore.QSize(DEFAULT_SIZE, DEFAULT_SIZE))
            # self.SID1Layout.setSpacing(0)
            # self.SID1Layout.setContentsMargins(0, 0, 0, 0)
            # self.SID2Layout.setSpacing(0)
            # self.SID2Layout.setContentsMargins(0, 0, 0, 0)
            self.AcelLayout.setSpacing(5)
            self.AcelLayout.setContentsMargins(0, 0, 0, 0)

    def buttonHandlers(self, mode):
      #  print (mode)
        if mode == "Off":
            self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)  
            self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)  
            self.leftButton1.setIcon(QIcon(LEFT1_ICON))
            self.rightButton1.setIcon(QIcon(RIGHT1_ICON))
            self.leftButton2.setIcon(QIcon(LEFT2_ICON))
            self.rightButton2.setIcon(QIcon(RIGHT2_ICON))
            self.leftButton3.setIcon(QIcon(LEFT3_ICON))
            self.rightButton3.setIcon(QIcon(RIGHT3_ICON))
            self.leftButton4.setIcon(QIcon(LEFT4_ICON))
            self.rightButton4.setIcon(QIcon(RIGHT4_ICON))


        if mode == "Mode 1":
            self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton1.setStyleSheet(GUI_Style.buttonPressed) 
            self.leftButton1.setIcon(QIcon(LEFT1_ICON_PRES))
            self.rightButton1.setIcon(QIcon(RIGHT1_ICON_PRES))       
        if mode == "Mode 2":
            self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)    
            self.leftButton2.setIcon(QIcon(LEFT2_ICON_PRES))
            self.rightButton2.setIcon(QIcon(RIGHT2_ICON_PRES))
        if mode == "Mode 3":
            self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.leftButton3.setIcon(QIcon(LEFT3_ICON_PRES))
            self.rightButton3.setIcon(QIcon(RIGHT3_ICON_PRES))
        if mode == "Mode 4":
            self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
            self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton4.setIcon(QIcon(LEFT4_ICON_PRES))
            self.rightButton4.setIcon(QIcon(RIGHT4_ICON_PRES))
        if mode == "Mode 5":
            # ~ pass
            self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton1.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)        
            self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)  
            self.rightButton3.setStyleSheet(GUI_Style.buttonPressed) 
            self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
            self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
            self.leftButton1.setIcon(QIcon(LEFT1_ICON_PRES))
            self.rightButton1.setIcon(QIcon(RIGHT1_ICON_PRES)) 
            self.leftButton2.setIcon(QIcon(LEFT2_ICON_PRES))
            self.rightButton2.setIcon(QIcon(RIGHT2_ICON_PRES))
            self.leftButton3.setIcon(QIcon(LEFT3_ICON_PRES))
            self.rightButton3.setIcon(QIcon(RIGHT3_ICON_PRES))
            self.leftButton4.setIcon(QIcon(LEFT4_ICON_PRES))
            self.rightButton4.setIcon(QIcon(RIGHT4_ICON_PRES))

    def Button1_Clicked(self):
        self.leftButton1.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton1.setStyleSheet(GUI_Style.buttonPressed)        
        self.leftButton1.setIcon(QIcon(LEFT1_ICON_PRES))
        self.rightButton1.setIcon(QIcon(RIGHT1_ICON_PRES))
        # self.GPIOthread.SWpushButton("Mode 1")
        self.updateAccelerometer(90,1,1)

    def Button1_Released(self):
        self.leftButton1.setIcon(QIcon(LEFT1_ICON))
        self.rightButton1.setIcon(QIcon(RIGHT1_ICON))
        self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)        
        # self.GPIOthread.SWpushButton("Off")
        
    def Button2_Clicked(self):
        self.leftButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton2.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton2.setIcon(QIcon(LEFT2_ICON_PRES))
        self.rightButton2.setIcon(QIcon(RIGHT2_ICON_PRES))
        # self.GPIOthread.SWpushButton("Mode 2")
        self.updateAccelerometer(0,1,1)


    def Button2_Released(self):
        self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setIcon(QIcon(LEFT2_ICON))
        self.rightButton2.setIcon(QIcon(RIGHT2_ICON))
        # self.GPIOthread.SWpushButton("Off")

    def Button3_Clicked(self):
        self.leftButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton3.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton3.setIcon(QIcon(LEFT3_ICON_PRES))
        self.rightButton3.setIcon(QIcon(RIGHT3_ICON_PRES))
        # self.GPIOthread.SWpushButton("Mode 3")
        self.updateAccelerometer(-90,1,1)


    def Button3_Released(self):
        self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setIcon(QIcon(LEFT3_ICON))
        self.rightButton3.setIcon(QIcon(RIGHT3_ICON))
        # self.GPIOthread.SWpushButton("Off")

    def Button4_Clicked(self):
        self.leftButton4.setStyleSheet(GUI_Style.buttonPressed)
        self.rightButton4.setStyleSheet(GUI_Style.buttonPressed)
        self.leftButton4.setIcon(QIcon(LEFT4_ICON_PRES))
        self.rightButton4.setIcon(QIcon(RIGHT4_ICON_PRES))
        self.GPIOthread.SWpushButton("Mode 4")

    def Button4_Released(self):
        self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton4.setIcon(QIcon(LEFT4_ICON))
        self.rightButton4.setIcon(QIcon(RIGHT4_ICON))
        self.GPIOthread.SWpushButton("Off")

    # ------------------------------------------------------------------
    # ----------- Close All Threads at app closure ---------------------
    # ------------------------------------------------------------------             
    # Stop all threads when GUI is closed
    def closeEvent(self, *args, **kwargs):
        self.GPIOthread.terminate()
        self.GPIOthread.wait(100)        
        self.accelerometer.terminate()
        self.accelerometer.wait(100)       
        self.ADC.terminate()
        self.ADC.wait(100)
        GPIO.cleanup()
        sys.exit(0)

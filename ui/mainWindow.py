# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_mainWindow import Ui_MainWindow

from PyQt5 import QtWidgets

from PyQt5.QtGui import QPixmap
from threading import Event

from newValue import Controller,  ControlArduino    
        
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        scene = QtWidgets.QGraphicsScene()

        
        scene.addPixmap(QPixmap('Medicatech.png'))

        
        self.MediLogo.setScene(scene)


        self.stop_flag_time =  Event()
        self.stop_flag_RS232 =  Event()

        self.getController = Controller(self.stop_flag_time)
        self.getController.start()
        self.getController.newTime.connect(self.updateTime)
 
        self.getArduino = ControlArduino(self.stop_flag_RS232)
        self.getArduino.newValue.connect(self.updatePoti)  
        self.getArduino.testRS232.connect(self.updateInfoRS232)          
        self.getArduino.start() 
        
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.stop_flag_time.set()
        self.stop_flag_RS232.set()
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

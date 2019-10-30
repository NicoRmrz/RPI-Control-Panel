from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import datetime, time
import serial
value = 0
intwert = 0

class Controller(QThread, object):
    
    now = datetime.datetime.now()
    timeInterval="%0.2d:%0.2d" %(now.hour, now.minute)
    
    newTime = pyqtSignal(object)
    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event
        
    def run(self):
        while not self.stopped.wait(1):
            self.inTime1()
    
    def inTime1(self):
        global timeInterval
        now = datetime.datetime.now()
        timeInterval="%0.2d:%0.2d" %(now.hour, now.minute)
        self.newTime.emit(timeInterval)
        
class ControlArduino(QThread):
    newValue = pyqtSignal(object, object, object)
    testRS232 = pyqtSignal(object)
    
    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event
        self.altValue = 0
        
    def run(self):
        try:
            self.serArduino = serial.Serial('/dev/ttyADM0', 115200, timeout=0)
            self.noRS232_UNO = 1
            self.testRS232.emit(1)
            
        except:
            print("RS232 for Arduino not found")
            self.noRS232_UNO = 0
            self.testRS232.emit(0)
            
        while not self.stopped.wait(0.01):
            self.ArduinoLoop()
    def ArduinoLoop(self):
        global intwert
        global value
        if self.noRS232_UNO:
            self.serArduino.write(b'p')
            time.sleep(0.01)
            wert = self.serArduino.read(16)
            try:
                wert1 = wert.split()
                intwert = int(wert1[0])
                intwert1 = int(wert1[1])
                intwert2 = int(wert1[2])
                value = int(22 +(intwert/3.84))
                self.newValue.emit(intwert, intwert1, intwert2)
                
                print(intwert)
            except:
                print("Error Arduino Serial")
        
        

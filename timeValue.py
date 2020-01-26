from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import datetime, time
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
        # ~ timeInterval= datetime.datetime.now().strftime('%d %B %Y %I:%M:%S')
        # ~ timeInterval= datetime.datetime.now().strftime('%I:%M:%S %p')
        
        self.newTime.emit(timeInterval)
   
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import datetime, time
import pytz

#-------------------------------
# Select Timezone
#-------------------------------
# TIME_ZONE = "US/Alaska"
# TIME_ZONE = "US/Arizona"
# TIME_ZONE = "US/Central"
# TIME_ZONE = "US/East-Indiana"
# TIME_ZONE = "US/Eastern"
# TIME_ZONE = "US/Hawaii"
# TIME_ZONE = "US/Indiana-Starke"
# TIME_ZONE = "US/Michigan"
TIME_ZONE = "US/Mountain"
# TIME_ZONE = "US/Pacific"
# TIME_ZONE = "US/Samoa"
#-------------------------------
#-------------------------------
#-------------------------------

class Controller(QThread, object):
    
    newTime = pyqtSignal(object)
    fmt = '%H:%M'

    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event
        
    def run(self):
        while not self.stopped.wait(1):
            self.inTime1()
    
    def inTime1(self):
        global timeInterval
        now = datetime.datetime.now()
        
        timezone = pytz.timezone(TIME_ZONE)
        test = datetime.datetime.now(timezone)
        timeInterval = test.strftime(self.fmt)
        
        self.newTime.emit(timeInterval)
   
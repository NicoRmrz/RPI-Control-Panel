from PyQt5.QtCore import QPoint, Qt, QTime, QTimer, QRectF
from PyQt5.QtGui import QColor, QPainter, QPolygon, QPen, QFontMetricsF, QFont
from PyQt5.QtWidgets import QApplication, QWidget

ANGLEREADING = 0

class angleGraphic(QWidget):
    moveTick = 0
    measHand = QPolygon([
        QPoint(15, 0),
        QPoint(-15, 0),
        QPoint(0, -100)
    ])

    PURP = QColor(127, 0, 127)
    TEAL = QColor(0, 127, 127, 191)
    LIGHTBLUE = QColor(123, 177, 223, 255)
    WHITE = QColor(255,255,255,75)
    HARD_WHITE = QColor(255,255,255,200)
    YELLOW = QColor(255, 253, 208, 200)
    YELLOW_CIRCLE = QColor(255, 253, 208, 150)
    YELLOW_FULL = QColor(255, 253, 208, 240)

    # ~ degMarker = 15
    # ~ angleText = {0: "0", 15:"-15", 30: "-30", 45: "-45", 60: "-60", 75: "-75", 90: "-90", 105:"105", 120:"120", 135: "45", 150:"150", 165:"165", 180: "0", 195: "-15", 210: "210", 225: "-45", 240:"240", 255:"255", 270: "90", 285:"75", 300:"69", 315: "45", 330:"30", 345:"15"}

    degMarker = 30
    angleText = {0: "0", 30: "-30", 60: "-60", 90: "-90", 120:"-60", 150:"-30",180: "0", 210: "-30", 240:"-60", 270: "90", 300:"60",  330:"30"}
	
    # degMarker = 45
    # angleText = {0: "0", 45: "45", 90: "90", 135: "45", 180: "0", 225: "-45", 270: "-90", 315: "315"}
    
#     degMarker = 90
#     angleText = {0: "0", 90: "90",  180: "0",270: "-90"}
    
    tickMarks = 2	# every tick per degree
	
    def __init__(self, parent=None):
        super(angleGraphic, self).__init__(parent)
        self.setMinimumSize(500, 325)
        self.setMaximumSize(500, 325)

    def setAngleTick(self, reading):
    	self.moveTick = reading

    def setScreenOrientation (self, orientaion):
    	self.POS = orientaion

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        font = QFont(self.font())
        font.setPixelSize(9)
	# ~ font.setW
        metrics = QFontMetricsF(font)

        # ----------------------------------
        # ----------- Normal  --------------
        # ----------------------------------
        if (self.POS == "Normal"):
        	self.setMinimumSize(500, 325)
        	self.setMaximumSize(500, 325)
        	val = 180 - self.moveTick 

        	painter.translate(self.width() / 2, self.height() / 9)
        	painter.scale(side / 160.0, side / 140.0)

        # ----------------------------------
        # ------------ Right ---------------
        # ----------------------------------
        elif (self.POS == "Right"):
        	self.setMinimumSize(450, 325)
        	self.setMaximumSize(450, 325)
        	val = 180 - self.moveTick + 45

        	painter.scale(side / 190.0, side / 140.0)
        	painter.translate(self.width() / 3.5, self.height() / 20)

        # ----------------------------------
        # ------------- Left ---------------
        # ----------------------------------
        elif (self.POS == "Left"):
        	self.setMinimumSize(450, 325)
        	self.setMaximumSize(450, 325)
        	val = 180 - self.moveTick - 45

        	painter.scale(side / 190.0, side / 140.0)
        	painter.translate(self.width() / 3.5, self.height() / 20)
		
	# ----------------------------------
	# -------- Draw On Painter ---------
        # ----------------------------------
	# Draw top line 
        pen = QPen()
        pen.setWidth(15)
        pen.setBrush(angleGraphic.LIGHTBLUE)
        painter.setPen(pen)
        for i in range(90):
                painter.drawLine(1 ,0 , 100, 0)
                painter.rotate(180.0)

	# Measurement Hand
        painter.setPen(Qt.NoPen)
        painter.setBrush(angleGraphic.YELLOW_FULL)
        painter.save()
        painter.rotate(val)
        painter.drawConvexPolygon(angleGraphic.measHand)
        painter.restore()

	# Middle Circle
        painter.setPen(angleGraphic.YELLOW_CIRCLE)
        i = 0
        while i < 360:
                painter.drawLine(0, 0, 15, 0)
                painter.rotate(1)  
                i += 1
	    
	# Tick marks
        painter.setPen(angleGraphic.WHITE)
        i = 0
        while i < 180:
                painter.drawLine(40, 0, 100, 0)
                painter.rotate(self.tickMarks)
                i += self.tickMarks

	# Angle Text
        painter.setPen(angleGraphic.HARD_WHITE)
        i = 0
        while i < 360:
                if (i % self.degMarker  == 0):
                        painter.drawLine(95, 0, 100, 0)
                        painter.drawText(-metrics.width(self.angleText[i])/1, -110, self.angleText[i])
                else:
                        pass
                painter.rotate(15)
                i += 15
		
	# Update paint
        self.update()

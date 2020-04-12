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
    HARD_WHITE = QColor(255,255,255,255)
    YELLOW = QColor(255, 253, 208, 200)

    # degMarker = 15
    # angleText = {0: "0", 15:"15", 30: "30", 45: "45", 60: "60", 75: "75", 90: "90", 105:"105", 120:"120", 135: "45", 150:"150", 165:"165", 180: "0", 195: "-15", 210: "210", 225: "-45", 240:"240", 255:"255", 270: "-90", 285:"285", 300:"300", 315: "315", 330:"330", 345:"345"}

    degMarker = 30
    angleText = {0: "0", 30: "-30", 60: "-60", 90: "-90", 120:"-60", 150:"-30",180: "0", 210: "-30", 240:"-60", 270: "90", 300:"60",  330:"30"}
	
    # degMarker = 45
    # angleText = {0: "0", 45: "45", 90: "90", 135: "45", 180: "0", 225: "-45", 270: "-90", 315: "315"}
	
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
        font.setPixelSize(10)
        metrics = QFontMetricsF(font)

        # ----------------------------------
        # ----------- Normal  --------------
        # ----------------------------------
        if (self.POS == "Normal"):
        	val = 180 - self.moveTick 

        	painter.translate(self.width() / 2, self.height() / 20)
        	painter.scale(side / 160.0, side / 140.0)

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
	        painter.setBrush(angleGraphic.YELLOW)
	        painter.save()
	        painter.rotate(val)
	        painter.drawConvexPolygon(angleGraphic.measHand)
	        painter.restore()

			# Tick marks
	        painter.setPen(angleGraphic.WHITE)
	        for j in range(180):
	            if (j % 2) != 0:
	                painter.drawLine(40, 0, 100, 0)
	            painter.rotate(1)

			# Angle Text
	        painter.setPen(angleGraphic.HARD_WHITE)
	        i = 0
	        while i < 360:
	            if (i % self.degMarker  == 0):
	                painter.drawLine(40, 0, 105, 0)
	                painter.drawText(-metrics.width(self.angleText[i])/1.5, -110, self.angleText[i])
	            else:
	                pass
	            painter.rotate(15)
	            i += 15

        # ----------------------------------
        # ------------ Right ---------------
        # ----------------------------------
        elif (self.POS == "Right"):

        	val = 180 - self.moveTick + 47

        	painter.scale(side / 180.0, side / 140.0)
        	painter.translate(self.width() / 4, self.height() / 30)

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
	        painter.setBrush(angleGraphic.YELLOW)
	        painter.save()
	        painter.rotate(val)
	        painter.drawConvexPolygon(angleGraphic.measHand)
	        painter.restore()

            # Tick marks
	        painter.setPen(angleGraphic.WHITE)
	        for j in range(180):
	            if (j % 2) != 0:
	                painter.drawLine(40, 0, 100, 0)
	            painter.rotate(1)


			# Angle Text
	        painter.setPen(angleGraphic.HARD_WHITE)
	        i = 0
	        while i < 360:
	            if (i % self.degMarker  == 0):
	                painter.drawLine(40, 0, 105, 0)
	                painter.drawText(-metrics.width(self.angleText[i])/1.5, -110, self.angleText[i])
	            else:
	                pass
	            painter.rotate(15)
	            i += 15

        # ----------------------------------
        # ------------- Left ---------------
        # ----------------------------------
        elif (self.POS == "Left"):
        	val = 180 - self.moveTick - 47

        	painter.scale(side / 160.0, side / 140.0)
        	painter.translate(self.width() / 4, self.height() / 30)

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
	        painter.setBrush(angleGraphic.YELLOW)
	        painter.save()
	        painter.rotate(val)
	        painter.drawConvexPolygon(angleGraphic.measHand)
	        painter.restore()

            # Tick marks
	        painter.setPen(angleGraphic.WHITE)
	        for j in range(180):
	            if (j % 2) != 0:
	                painter.drawLine(40, 0, 100, 0)
	            painter.rotate(1)

			# Angle Text
	        painter.setPen(angleGraphic.HARD_WHITE)
	        i = 0
	        while i < 360:
	            if (i % self.degMarker  == 0):
	                painter.drawLine(40, 0, 105, 0)
	                painter.drawText(-metrics.width(self.angleText[i])/1.5, -110, self.angleText[i])
	            else:
	                pass
	            painter.rotate(15)
	            i += 15


        self.update()

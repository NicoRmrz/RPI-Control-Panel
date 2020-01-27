from PyQt5.QtCore import QPoint, Qt, QTime, QTimer, QRectF
from PyQt5.QtGui import QColor, QPainter, QPolygon, QPen
from PyQt5.QtWidgets import QApplication, QWidget

ANGLEREADING = 0

class angleGraphic(QWidget):

    measHand = QPolygon([
        QPoint(15, 0),
        QPoint(-15, 0),
        QPoint(0, -100)
    ])

    PURP = QColor(127, 0, 127)
    TEAL = QColor(0, 127, 127, 191)
    LIGHTBLUE = QColor(123, 177, 223, 255)
    WHITE = QColor(255,255,255,75)
    YELLOW = QColor(255, 253, 208, 200)


    def __init__(self, parent=None):
        super(angleGraphic, self).__init__(parent)
        self.setMinimumSize(150, 175)
        self.setMaximumSize(200, 200)

    def setAngleTick(self, reading):
    	self.moveTick = reading

    def setScreenOrientation (self, orientaion):
    	self.POS = orientaion


    def paintEvent(self, event):
        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        val = 180 - self.moveTick
        print(val)

        if (self.POS == "Normal"):
	        self.setMinimumSize(150, 175)
        	self.setMaximumSize(200, 200)
        	painter.translate(self.width() / 2, self.height() / 50)
        	painter.scale(side / 220.0, side / 130.0)

	        # Draw top line 
	        pen = QPen()
	        pen.setWidth(15)
	        pen.setBrush(angleGraphic.LIGHTBLUE);
	        painter.setPen(pen)
	        for i in range(90):
	            painter.drawLine(1 ,0 , 100, 0)
	            painter.rotate(180.0)

	        # Measurement Hand
	        painter.setPen(Qt.NoPen)
	        painter.setBrush(angleGraphic.YELLOW)
	        painter.save()

	        #self.moveTick = 180 - self.moveTick
	        painter.rotate(val)
	        painter.drawConvexPolygon(angleGraphic.measHand)
	        painter.restore()


            # Tick marks
	        painter.setPen(angleGraphic.WHITE)

	        for j in range(180):
	            if (j % 2) != 0:
	                painter.drawLine(40, 0, 100, 0)
	            painter.rotate(2.0)

        elif (self.POS == "Right"):

       		self.setMinimumSize(175, 175)
        	self.setMaximumSize(200, 200)

        	painter.scale(side / 220.0, side / 130.0)
        	painter.translate(self.width() / 1.70, self.height() / 30)

	        # Draw top line 
	        pen = QPen()
	        pen.setWidth(15)
	        pen.setBrush(angleGraphic.LIGHTBLUE);
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
	            painter.rotate(2.0)

        elif (self.POS == "Left"):

       		self.setMinimumSize(175, 175)
        	self.setMaximumSize(250, 250)

        	painter.scale(side / 220.0, side / 130.0)
        	painter.translate(self.width() / 1.7, self.height() / 30)

	        # Draw top line 
	        pen = QPen()
	        pen.setWidth(15)
	        pen.setBrush(angleGraphic.LIGHTBLUE);
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
	            painter.rotate(2.0)


        self.update()

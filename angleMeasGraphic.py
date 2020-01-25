from PyQt5.QtCore import QPoint, Qt, QTime, QTimer, QRectF
from PyQt5.QtGui import QColor, QPainter, QPolygon, QPen
from PyQt5.QtWidgets import QApplication, QWidget

class angleGraphic(QWidget):
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -40)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])

    hourColor = QColor(127, 0, 127)
    minuteColor = QColor(0, 127, 127, 191)

    def __init__(self, parent=None):
        super(angleGraphic, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setMinimumSize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height())


        time = QTime.currentTime()

        painter = QPainter(self)
        #painter.begin(self)

        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)
        painter.drawArc(15, 15, 70, 70, 0 * 16, -180 * 16)         # <-----------        

        painter.setPen(Qt.NoPen)
        painter.setBrush(angleGraphic.hourColor)



        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(angleGraphic.hourHand)
        painter.restore()

        pen = QPen()
        pen.setWidth(3)
        pen.setBrush(angleGraphic.hourColor);

        # painter.setPen(angleGraphic.hourColor)
        painter.setPen(pen)

        for i in range(90):
            painter.drawLine(1 ,0 , 90, 0)
            painter.rotate(180.0)


        painter.setPen(Qt.NoPen)
        painter.setBrush(angleGraphic.minuteColor)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(angleGraphic.minuteHand)
        painter.restore()

        painter.setPen(angleGraphic.minuteColor)


        for j in range(30):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)


        # make a white drawing background
        # painter.setBrush(Qt.white)
        # painter.drawRect(event.rect())


        painter.setPen(Qt.green)
        painter.setBrush(Qt.white)
    #   # painter.drawArc(100, 70, 300, 300, 0 * 16, 180 * 16)
    #     # upside down
        #painter.drawArc(100, 70, 175, 175, 0 * 16, -180 * 16)
        #painter.drawArc(15, 15, 70, 70, 0 * 16, -180 * 16)         # <-----------        

        painter.setPen(QPen(Qt.red))
    #     painter.restore()
        painter.end()


        self.update()




    # def paintEvent(self, event):
    #     side = min(self.width(), self.height())

    #     painter = QPainter()
    #     painter.begin(self)
      
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.setPen(Qt.green)
    #     painter.setBrush(Qt.white)
    #   # painter.drawArc(100, 70, 300, 300, 0 * 16, 180 * 16)
    #     # upside down
    #     painter.save()

    #     painter.drawArc(100, 70, 300, 300, 0 * 16, -180 * 16)
    #     painter.setPen(QPen(Qt.red))
    #     painter.restore()

      
    #     painter.end()


    #     self.update()

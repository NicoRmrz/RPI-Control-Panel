# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USMedimade\Documents\Eric Works\MX30 GUI\ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QStatusBar, QLabel
from PyQt5.QtCore import Qt

# User made files
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()




# Icon Image locations
Main_path = os.getcwd() + "/"
xray1_Path = Main_path + "/icons/ray.png"
closex64_Path = Main_path + "/icons/Button-Close-icon x 64.png"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(xray1_Path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        MainWindow.setWindowIcon(QIcon(xray1_Path))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setTabletTracking(True)
        self.centralWidget.setStyleSheet("background-color: rgb(58, 213, 255);")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 24pt \"Arial\";")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 7, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lblAnzeige2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAnzeige2.sizePolicy().hasHeightForWidth())
        self.lblAnzeige2.setSizePolicy(sizePolicy)
        self.lblAnzeige2.setStyleSheet("font: 36pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblAnzeige2.setScaledContents(True)
        self.lblAnzeige2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAnzeige2.setObjectName("lblAnzeige2")
        self.gridLayout.addWidget(self.lblAnzeige2, 5, 6, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 24pt \"Arial\";")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 24pt \"Arial\";")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 6, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lblAnzeige3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAnzeige3.sizePolicy().hasHeightForWidth())
        self.lblAnzeige3.setSizePolicy(sizePolicy)
        self.lblAnzeige3.setStyleSheet("font: 36pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblAnzeige3.setScaledContents(True)
        self.lblAnzeige3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAnzeige3.setObjectName("lblAnzeige3")
        self.gridLayout.addWidget(self.lblAnzeige3, 5, 7, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblRSinfo = QtWidgets.QLabel(self.centralWidget)
        self.lblRSinfo.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblRSinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRSinfo.setObjectName("lblRSinfo")
        self.gridLayout.addWidget(self.lblRSinfo, 6, 6, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lbltime = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltime.sizePolicy().hasHeightForWidth())
        self.lbltime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbltime.setFont(font)
        self.lbltime.setStyleSheet("font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lbltime.setText("")
        self.lbltime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbltime.setObjectName("lbltime")
        self.gridLayout.addWidget(self.lbltime, 2, 9, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.lblAnzeige = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAnzeige.sizePolicy().hasHeightForWidth())
        self.lblAnzeige.setSizePolicy(sizePolicy)
        self.lblAnzeige.setStyleSheet("font: 36pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblAnzeige.setScaledContents(True)
        self.lblAnzeige.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAnzeige.setObjectName("lblAnzeige")
        self.gridLayout.addWidget(self.lblAnzeige, 5, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.StatusBar()
        self.setStatusBar(self.statusBar)

        self.MediLogo = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MediLogo.sizePolicy().hasHeightForWidth())
        self.MediLogo.setSizePolicy(sizePolicy)
        self.MediLogo.setMinimumSize(QtCore.QSize(378, 78))
        self.MediLogo.setMaximumSize(QtCore.QSize(759, 159))
        self.MediLogo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(255, 255, 255, 0);\n"
"color: rgba(255, 255, 255, 0);\n"
"alternate-background-color: rgba(255, 255, 255, 0);\n"
"gridline-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.MediLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MediLogo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MediLogo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MediLogo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.MediLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.MediLogo.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.MediLogo.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.MediLogo.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.MediLogo.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.MediLogo.setOptimizationFlags(QtWidgets.QGraphicsView.DontClipPainter)
        self.MediLogo.setObjectName("MediLogo")
        self.gridLayout.addWidget(self.MediLogo, 2, 3, 1, 4, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 8, 1, 2)
        self.btnExit = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMinimumSize(QtCore.QSize(67, 67))
        self.btnExit.setMaximumSize(QtCore.QSize(67, 67))
        self.btnExit.setAutoFillBackground(False)
        self.btnExit.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"background-image: url(icons/Button-Close-icon x 64.png)\n"
"")
        self.btnExit.setText("")
        self.btnExit.setIconSize(QtCore.QSize(200, 200))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setDefault(False)
        self.btnExit.setFlat(False)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 6, 9, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 3, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 7, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 7, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 8, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 3, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)





        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MX30 GUI"))
        self.label_4.setText(_translate("MainWindow", "SID3"))
        self.lblAnzeige2.setText(_translate("MainWindow", "1000"))
        self.label_2.setText(_translate("MainWindow", "SID"))
        self.label_3.setText(_translate("MainWindow", "SID2"))
        self.lblAnzeige3.setText(_translate("MainWindow", "1000"))
        self.lblRSinfo.setText(_translate("MainWindow", "Poti on A0"))
        self.lblAnzeige.setText(_translate("MainWindow", "1000"))

    # ------------------------------------------------------------------
    # ---------------- Create Status Bar Functions ----------------------
    # ------------------------------------------------------------------
    def StatusBar(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet(GUI_Style.statusBarWhite)
        
        self.xAxis = QLabel()
        self.xAxis.setMinimumSize(50, 12)
        self.xAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.xAxis.setText("x-axis")
        self.xAxis.setAlignment(Qt.AlignCenter)
        
        self.yAxis = QLabel()
        self.yAxis.setMinimumSize(50, 12)
        self.yAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.yAxis.setText("y-axis")
        self.yAxis.setAlignment(Qt.AlignCenter)
        
        self.zAxis = QLabel()
        self.zAxis.setMinimumSize(50, 15)
        self.zAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.zAxis.setText("z-axis")
        self.zAxis.setAlignment(Qt.AlignCenter)
        
        self.statusBar.addPermanentWidget(self.xAxis, 0)
        self.statusBar.addPermanentWidget(self.yAxis, 0)
        self.statusBar.addPermanentWidget(self.zAxis, 0)
        
        self.statusBar.showMessage("Initializing... ", 4000)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


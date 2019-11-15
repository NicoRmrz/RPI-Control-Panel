# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USMedimade\Documents\Eric Works\MX30 GUI\ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QStatusBar, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

# User made files
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()


# Icon Image locations
Main_path = os.getcwd() + "/"
xray1_Path = Main_path + "/icons/ray.png"
closex64_Path = Main_path + "/icons/exit.png"
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
        self.centralWidget.setStyleSheet(GUI_Style.mainWidget)
        self.centralWidget.setObjectName("centralWidget")


        # ---------------------------------------------------------------------
        # ----------------------- Header Layout -------------------------------
        # ---------------------------------------------------------------------
        self.HeaderLayout = QtWidgets.QHBoxLayout()
        self.HeaderLayout.setSpacing(0)
        self.HeaderLayout.setContentsMargins(0, 0, 0, 0)

        # Logo
        self.MediLogo = QtWidgets.QGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MediLogo.sizePolicy().hasHeightForWidth())
        self.MediLogo.setSizePolicy(sizePolicy)
        self.MediLogo.setMinimumSize(QtCore.QSize(378, 78))
        self.MediLogo.setMaximumSize(QtCore.QSize(759, 159))
        self.MediLogo.setStyleSheet(GUI_Style.logo)
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

        self.logoscene = QtWidgets.QGraphicsScene()

        self.logoscene.addPixmap(QPixmap(Mediatech_Path))

        self.MediLogo.setScene(self.logoscene)



        # Timer
        self.clockTime = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clockTime.sizePolicy().hasHeightForWidth())
        self.clockTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clockTime.setFont(font)
        self.clockTime.setStyleSheet(GUI_Style.timer)
        self.clockTime.setText("")
        self.clockTime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.clockTime.setObjectName("clockTime")
        self.clockTime.setMinimumSize(150, 50)

        # Create Graphics view object to rotate widgets
        self.timeView = QtWidgets.QGraphicsView()
        self.timeView.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.timeScene = QtWidgets.QGraphicsScene(self.timeView)
        self.timeView.setScene(self.timeScene)
        self.timeScene.addWidget(self.clockTime)



        self.btnExit = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMinimumSize(QtCore.QSize(67, 67))
        self.btnExit.setMaximumSize(QtCore.QSize(67, 67))
        self.btnExit.setAutoFillBackground(False)
        self.btnExit.setStyleSheet(GUI_Style.exitBtn)
        self.btnExit.setText("")
        self.btnExit.setIcon(QIcon(closex64_Path))
        self.btnExit.setIconSize(QtCore.QSize(45, 45))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setDefault(False)
        self.btnExit.setFlat(False)
        self.btnExit.setObjectName("btnExit")

        # Create Graphics view object to rotate widgets
        self.exitBtn_View = QtWidgets.QGraphicsView()
        self.exitBtn_View.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.exitBtn_Scene = QtWidgets.QGraphicsScene(self.exitBtn_View)
        self.exitBtn_View.setScene(self.exitBtn_Scene)
        self.exitBtn_Scene.addWidget(self.btnExit)

        self.HeaderLayout.addWidget(self.MediLogo, Qt.AlignLeft)
        self.HeaderLayout.addWidget(self.timeView, Qt.AlignRight)
        self.HeaderLayout.addWidget(self.exitBtn_View)



        # ---------------------------------------------------------------------
        # -------------------- SID Layouts ------------------------------------
        # ---------------------------------------------------------------------
        # ----------------------------------
        # ------------ SID 1 ---------------
        # ----------------------------------
        self.SID1Layout = QtWidgets.QHBoxLayout()
        self.SID1Layout.setSpacing(0)
        self.SID1Layout.setContentsMargins(0, 0, 0, 0)       

        # Create Left Button 1
        self.leftButton1 = QtWidgets.QPushButton()
        self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton1.setMinimumSize(60,60)
        self.leftButton1.setIcon(QIcon(Rotate_Idle))
        self.leftButton1.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.LBtn1_View = QtWidgets.QGraphicsView()
        self.LBtn1_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn1_Scene = QtWidgets.QGraphicsScene(self.LBtn1_View)
        self.LBtn1_View.setScene(self.LBtn1_Scene)
        self.LBtn1_Scene.addWidget(self.leftButton1)

        # Create SID Label
        self.SID1_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID1_label.sizePolicy().hasHeightForWidth())
        self.SID1_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SID1_label.setFont(font)
        self.SID1_label.setStyleSheet(GUI_Style.SID)
        self.SID1_label.setScaledContents(True)
        self.SID1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SID1_label.setObjectName("SID1_label")
        self.SID1_label.setMinimumWidth(75)

        # Create Graphics view object to rotate widgets
        self.SID1Label_View = QtWidgets.QGraphicsView()
        self.SID1Label_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID1Label_Scene = QtWidgets.QGraphicsScene(self.SID1Label_View)
        self.SID1Label_View.setScene(self.SID1Label_Scene)
        self.SID1Label_Scene.addWidget(self.SID1_label)

        # Create SID Data field
        self.SID1_Data = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID1_Data.sizePolicy().hasHeightForWidth())
        self.SID1_Data.setSizePolicy(sizePolicy)
        self.SID1_Data.setStyleSheet(GUI_Style.SID_Data)
        self.SID1_Data.setScaledContents(True)
        self.SID1_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.SID1_Data.setObjectName("SID1_Data")
      
        # Create Graphics view object to rotate widgets
        self.SID1Data_View = QtWidgets.QGraphicsView()
        self.SID1Data_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID1Data_Scene = QtWidgets.QGraphicsScene(self.SID1Data_View)
        self.SID1Data_View.setScene(self.SID1Data_Scene)
        self.SID1Data_Scene.addWidget(self.SID1_Data)

        # Add objects to layout
        self.SID1Layout.addWidget(self.LBtn1_View)
        self.SID1Layout.addWidget(self.SID1Label_View)
        self.SID1Layout.addWidget(self.SID1Data_View, 1, Qt.AlignLeft)



        # ----------------------------------
        # ------------ SID 2 ---------------       
        # ----------------------------------
        self.SID2Layout = QtWidgets.QHBoxLayout()
        self.SID2Layout.setSpacing(0)
        self.SID2Layout.setContentsMargins(0, 0, 0, 0)  

        # Create Left Button 2
        self.leftButton2 = QtWidgets.QPushButton()
        self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setMinimumSize(60,60)
        self.leftButton2.setIcon(QIcon(Left_Idle))
        self.leftButton2.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.LBtn2_View = QtWidgets.QGraphicsView()
        self.LBtn2_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn2_Scene = QtWidgets.QGraphicsScene(self.LBtn2_View)
        self.LBtn2_View.setScene(self.LBtn2_Scene)
        self.LBtn2_Scene.addWidget(self.leftButton2)

        # Create SID Label
        self.SID2_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID2_label.sizePolicy().hasHeightForWidth())
        self.SID2_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SID2_label.setFont(font)
        self.SID2_label.setStyleSheet(GUI_Style.SID)
        self.SID2_label.setScaledContents(True)
        self.SID2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SID2_label.setObjectName("SID2_label")
        self.SID2_label.setMinimumWidth(75)

        # Create Graphics view object to rotate widgets
        self.SID2Label_View = QtWidgets.QGraphicsView()
        self.SID2Label_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID2Label_Scene = QtWidgets.QGraphicsScene(self.SID2Label_View)
        self.SID2Label_View.setScene(self.SID2Label_Scene)
        self.SID2Label_Scene.addWidget(self.SID2_label)

        # Create SID Data field
        self.SID2_Data = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID2_Data.sizePolicy().hasHeightForWidth())
        self.SID2_Data.setSizePolicy(sizePolicy)
        self.SID2_Data.setStyleSheet(GUI_Style.SID_Data)
        self.SID2_Data.setScaledContents(True)
        self.SID2_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.SID2_Data.setObjectName("SID2_Data")
        

         # Create Graphics view object to rotate widgets
        self.SID2Data_View = QtWidgets.QGraphicsView()
        self.SID2Data_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID2Data_Scene = QtWidgets.QGraphicsScene(self.SID2Data_View)
        self.SID2Data_View.setScene(self.SID2Data_Scene)
        self.SID2Data_Scene.addWidget(self.SID2_Data)


        # Add objects to layout
        self.SID2Layout.addWidget(self.LBtn2_View)
        self.SID2Layout.addWidget(self.SID2Label_View)
        self.SID2Layout.addWidget(self.SID2Data_View, 1, Qt.AlignLeft)

        # ----------------------------------
        # ------------ SID 3 ---------------
        # ----------------------------------
        self.SID3Layout = QtWidgets.QHBoxLayout()
        self.SID3Layout.setSpacing(0)
        self.SID3Layout.setContentsMargins(0, 0, 0, 0)

        # Create Left Button 3
        self.leftButton3 = QtWidgets.QPushButton()
        self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setMinimumSize(60,60)
        self.leftButton3.setIcon(QIcon(Up_Idle))
        self.leftButton3.setIconSize(QtCore.QSize(60, 60))
        # Create Graphics view object to rotate widgets
        self.LBtn3_View = QtWidgets.QGraphicsView()
        self.LBtn3_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn3_Scene = QtWidgets.QGraphicsScene(self.LBtn3_View)
        self.LBtn3_View.setScene(self.LBtn3_Scene)
        self.LBtn3_Scene.addWidget(self.leftButton3)

        # Create SID Label
        self.SID3_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID3_label.sizePolicy().hasHeightForWidth())
        self.SID3_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SID3_label.setFont(font)
        self.SID3_label.setStyleSheet(GUI_Style.SID)
        self.SID3_label.setScaledContents(True)
        self.SID3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SID3_label.setObjectName("SID3_label")
        self.SID3_label.setMinimumWidth(75)

        # Create Graphics view object to rotate widgets
        self.SID3Label_View = QtWidgets.QGraphicsView()
        self.SID3Label_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID3Label_Scene = QtWidgets.QGraphicsScene(self.SID3Label_View)
        self.SID3Label_View.setScene(self.SID3Label_Scene)
        self.SID3Label_Scene.addWidget(self.SID3_label)

        # Create SID Data field
        self.SID3_Data = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID3_Data.sizePolicy().hasHeightForWidth())
        self.SID3_Data.setSizePolicy(sizePolicy)
        self.SID3_Data.setStyleSheet(GUI_Style.SID_Data)
        self.SID3_Data.setScaledContents(True)
        self.SID3_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.SID3_Data.setObjectName("SID3_Data")

        # Create Graphics view object to rotate widgets
        self.SID3Data_View = QtWidgets.QGraphicsView()
        self.SID3Data_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID3Data_Scene = QtWidgets.QGraphicsScene(self.SID3Data_View)
        self.SID3Data_View.setScene(self.SID3Data_Scene)
        self.SID3Data_Scene.addWidget(self.SID3_Data)

        # Add objects to layout
        self.SID3Layout.addWidget(self.LBtn3_View)
        self.SID3Layout.addWidget(self.SID3Label_View)
        self.SID3Layout.addWidget(self.SID3Data_View, 1, Qt.AlignLeft)

        # ----------------------------------
        # ---------- Left Button 4 ---------
        # ----------------------------------
        self.Left4Layout = QtWidgets.QHBoxLayout()
        self.Left4Layout.setSpacing(0)
        self.Left4Layout.setContentsMargins(0, 0, 0, 0)

        # Create Left Button 4
        self.leftButton4 = QtWidgets.QPushButton()
        self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton4.setMinimumSize(75,60)

        # Create Graphics view object to rotate widgets
        self.LBtn4_View = QtWidgets.QGraphicsView()
        self.LBtn4_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn4_Scene = QtWidgets.QGraphicsScene(self.LBtn4_View)
        self.LBtn4_View.setScene(self.LBtn4_Scene)
        self.LBtn4_Scene.addWidget(self.leftButton4)
        self.button4Layout = QtWidgets.QVBoxLayout()

        self.spacerItem1 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        self.Left4Layout.addWidget(self.LBtn4_View, 1, Qt.AlignLeft)
        self.Left4Layout.addItem(self.spacerItem1)
        self.Left4Layout.addItem(self.spacerItem2)

        # ---------------------------------------------------------------------
        # ----------------- Left Side Button Layout ---------------------------
        # ---------------------------------------------------------------------
        self.LeftButtonLayout = QtWidgets.QVBoxLayout()
        self.LeftButtonLayout.setSpacing(0)
        self.LeftButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftButtonLayout.addLayout(self.SID1Layout)
        self.LeftButtonLayout.addLayout(self.SID2Layout)
        self.LeftButtonLayout.addLayout(self.SID3Layout)
        self.LeftButtonLayout.addLayout(self.Left4Layout)




        # ---------------------------------------------------------------------
        # ----------------- Accelerometer Layout ------------------------------
        # ---------------------------------------------------------------------
        self.AcelLayout = QtWidgets.QVBoxLayout()
        self.AcelLayout.setSpacing(0)
        self.AcelLayout.setContentsMargins(0, 0, 0, 0)

        # Create X Axis label
        self.xAxis = QLabel()
        self.xAxis.setMinimumSize(50, 12)
        self.xAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.xAxis.setText("x-axis")
        # self.xAxis.setAlignment(Qt.AlignCenter)

        # Create Graphics view object to rotate widgets
        self.xAx_View = QtWidgets.QGraphicsView()
        self.xAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.xAx_Scene = QtWidgets.QGraphicsScene(self.xAx_View)
        self.xAx_View.setScene(self.xAx_Scene)
        self.xAx_Scene.addWidget(self.xAxis)
        
        # Create Y Axis label
        self.yAxis = QLabel()
        self.yAxis.setMinimumSize(50, 12)
        self.yAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.yAxis.setText("y-axis")
        # self.yAxis.setAlignment(Qt.AlignCenter)
        
        # Create Graphics view object to rotate widgets
        self.yAx_View = QtWidgets.QGraphicsView()
        self.yAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yAx_Scene = QtWidgets.QGraphicsScene(self.yAx_View)
        self.yAx_View.setScene(self.yAx_Scene)
        self.yAx_Scene.addWidget(self.yAxis)

        # Create Z Axis label
        self.zAxis = QLabel()
        self.zAxis.setMinimumSize(50, 15)
        self.zAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.zAxis.setText("z-axis")
        # self.zAxis.setAlignment(Qt.AlignCenter)

        # Create Graphics view object to rotate widgets
        self.zAx_View = QtWidgets.QGraphicsView()
        self.zAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.zAx_Scene = QtWidgets.QGraphicsScene(self.zAx_View)
        self.zAx_View.setScene(self.zAx_Scene)
        self.zAx_Scene.addWidget(self.zAxis)


        self.Accelerometer = QtWidgets.QGroupBox("Accelerometer")
        Vlayout = QtWidgets.QVBoxLayout()
        Vlayout.addWidget(self.xAx_View)
        Vlayout.addWidget(self.yAx_View)
        Vlayout.addWidget(self.zAx_View)
        Vlayout.setSpacing(5)
        Vlayout.setContentsMargins(0, 0, 0, 0)


        self.Accelerometer.setLayout(Vlayout)
        self.Accelerometer.setStyleSheet(GUI_Style.groupBox)
        self.Accelerometer.setMaximumSize(200, 150)

        self.AcelLayout.addWidget(self.Accelerometer)
        # self.AcelLayout.addWidget(self.yAx_View)
        # self.AcelLayout.addWidget(self.zAx_View)


        # ---------------------------------------------------------------------
        # ----------------- Right Side Button Layout --------------------------
        # ---------------------------------------------------------------------
        # Create Right Button 1
        self.rightButton1 = QtWidgets.QPushButton()
        self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton1.setMinimumSize(60,60)
        self.rightButton1.setIcon(QIcon(Rotate1_Idle))
        self.rightButton1.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.RBtn1_View = QtWidgets.QGraphicsView()
        self.RBtn1_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn1_Scene = QtWidgets.QGraphicsScene(self.RBtn1_View)
        self.RBtn1_View.setScene(self.RBtn1_Scene)
        self.RBtn1_Scene.addWidget(self.rightButton1)

        # Create Right Button 2
        self.rightButton2 = QtWidgets.QPushButton()
        self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton2.setMinimumSize(60,60)
        self.rightButton2.setIcon(QIcon(Right_Idle))
        self.rightButton2.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.RBtn2_View = QtWidgets.QGraphicsView()
        self.RBtn2_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn2_Scene = QtWidgets.QGraphicsScene(self.RBtn2_View)
        self.RBtn2_View.setScene(self.RBtn2_Scene)
        self.RBtn2_Scene.addWidget(self.rightButton2)

        # Create Right Button 3
        self.rightButton3 = QtWidgets.QPushButton()
        self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton3.setMinimumSize(60,60)
        self.rightButton3.setIcon(QIcon(Down_Idle))
        self.rightButton3.setIconSize(QtCore.QSize(60, 60))
        # Create Graphics view object to rotate widgets
        self.RBtn3_View = QtWidgets.QGraphicsView()
        self.RBtn3_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn3_Scene = QtWidgets.QGraphicsScene(self.RBtn3_View)
        self.RBtn3_View.setScene(self.RBtn3_Scene)
        self.RBtn3_Scene.addWidget(self.rightButton3)

        # Create Right Button 4
        self.rightButton4 = QtWidgets.QPushButton()
        self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton4.setMinimumSize(75,60)

        # Create Graphics view object to rotate widgets
        self.RBtn4_View = QtWidgets.QGraphicsView()
        self.RBtn4_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn4_Scene = QtWidgets.QGraphicsScene(self.RBtn4_View)
        self.RBtn4_View.setScene(self.RBtn4_Scene)
        self.RBtn4_Scene.addWidget(self.rightButton4)


        self.RightButtonLayout = QtWidgets.QVBoxLayout()
        self.RightButtonLayout.setSpacing(0)
        self.RightButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.RightButtonLayout.addWidget(self.RBtn1_View)
        self.RightButtonLayout.addWidget(self.RBtn2_View)
        self.RightButtonLayout.addWidget(self.RBtn3_View)
        self.RightButtonLayout.addWidget(self.RBtn4_View)



        # ---------------------------------------------------------------------
        # ----------------- Bottom Horizontal Layout --------------------------
        # ---------------------------------------------------------------------
        self.BottomLayout = QtWidgets.QHBoxLayout()
        self.BottomLayout.setSpacing(20)
        self.BottomLayout.setContentsMargins(0, 0, 0, 0)
        self.BottomLayout.addLayout(self.LeftButtonLayout, QtCore.Qt.AlignLeft)
        self.BottomLayout.addLayout(self.AcelLayout)
        self.BottomLayout.addLayout(self.RightButtonLayout)


        # ---------------------------------------------------------------------
        # ----------------- Final  Layout -------------------------------------
        # ---------------------------------------------------------------------
        self.FinalLayout = QtWidgets.QVBoxLayout()
        self.FinalLayout.setSpacing(0)
        self.FinalLayout.setContentsMargins(0, 0, 0, 0)
        self.FinalLayout.addLayout(self.HeaderLayout)
        self.FinalLayout.addLayout(self.BottomLayout)





        MainWindow.setCentralWidget(self.centralWidget)

        self.centralWidget.setLayout(self.FinalLayout)
        self.centralWidget.isWindow()


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MX30 GUI"))
        self.SID3_label.setText(_translate("MainWindow", "SID3"))
        self.SID2_Data.setText(_translate("MainWindow", "1000"))
        self.SID1_label.setText(_translate("MainWindow", "SID1"))
        self.SID2_label.setText(_translate("MainWindow", "SID2"))
        self.SID3_Data.setText(_translate("MainWindow", "1000"))
        self.SID1_Data.setText(_translate("MainWindow", "1000"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


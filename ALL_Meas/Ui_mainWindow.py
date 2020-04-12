# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QPixmap, QIcon, QPainter,QPolygon, QColor
from PyQt5.QtWidgets import QStatusBar, QLabel, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QPoint

# User made files
from GUI_Stylesheets import GUI_Stylesheets

GUI_Style = GUI_Stylesheets()
SIDWIDTH = 200

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
SID1_path = Main_path + "/icons/sid1.png"
SID2_path = Main_path + "/icons/sid2.png"
Rotate_path = Main_path + "/icons/rotate.png"
Telescope_Idle = Main_path + "/icons/Telescope_Idle.png"
Telescope1_Idle = Main_path + "/icons/Telescope1_Idle.png"
Telescope_Pressed = Main_path + "/icons/Telescope_Pressed.png"
Telescope1_Pressed = Main_path + "/icons/Telescope1_Pressed.png"
UpDown_Idle = Main_path + "/icons/UpDown_Idle.png"
UpDown_Pressed = Main_path + "/icons/UpDown_Pressed.png"
LeftRight_Idle = Main_path + "/icons/LeftRight_Idle.png" 
LeftRight_Pressed = Main_path + "/icons/LeftRight_Pressed.png"

# IDLE
LEFT1_ICON = UpDown_Idle
LEFT2_ICON = Rotate_Idle
LEFT3_ICON = Telescope_Idle
LEFT4_ICON = LeftRight_Idle
RIGHT1_ICON = UpDown_Idle
RIGHT2_ICON = Rotate1_Idle
RIGHT3_ICON = Telescope_Idle
RIGHT4_ICON = LeftRight_Idle

# PRESSED
LEFT1_ICON_PRES = UpDown_Pressed
LEFT2_ICON_PRES = Rotate_Pressed
LEFT3_ICON_PRES = Telescope_Pressed
LEFT4_ICON_PRES = LeftRight_Pressed
RIGHT1_ICON_PRES = UpDown_Pressed
RIGHT2_ICON_PRES = Rotate1_Pressed
RIGHT3_ICON_PRES = Telescope_Pressed
RIGHT4_ICON_PRES = LeftRight_Pressed

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        # ----------------------------------
        # ---------- Meditech Logo  --------
        # ----------------------------------
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
        self.pixLogo = QPixmap(Mediatech_Path)
        self.logoscene.addPixmap(self.pixLogo)

        self.MediLogo.setScene(self.logoscene)

        # ----------------------------------
        # ----------- Clock  ---------------
        # ----------------------------------
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
        self.clockTime.setMinimumSize(150, 40)
        self.clockTime.setMaximumWidth(150)
        self.clockTime.setMaximumHeight(40)

        # Create Graphics view object to rotate widgets
        self.timeView = QtWidgets.QGraphicsView()
        self.timeView.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.timeScene = QtWidgets.QGraphicsScene(self.timeView)
        self.timeView.setScene(self.timeScene)
        self.timeScene.addWidget(self.clockTime)

        # ----------------------------------
        # --------- Exit Button ------------
        # ----------------------------------
        self.btnExit = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMinimumSize(QtCore.QSize(57, 57))
        self.btnExit.setMaximumSize(QtCore.QSize(57, 57))
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

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        self.HeaderLayout = QtWidgets.QHBoxLayout()
        self.HeaderLayout.setSpacing(0)
        self.HeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLayout.addWidget(self.MediLogo, Qt.AlignLeft)
        self.HeaderLayout.addWidget(self.timeView, Qt.AlignRight)
        self.HeaderLayout.addWidget(self.exitBtn_View)

        # ---------------------------------------------------------------------
        # -------------------- SID 1 Layout -----------------------------------
        # ---------------------------------------------------------------------
        # SID 1 Image
        self.SID1img = QtWidgets.QGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID1img.sizePolicy().hasHeightForWidth())
        self.SID1img.setSizePolicy(sizePolicy)
        # self.SID1img.setMinimumSize(QtCore.QSize(100, 100))
        self.SID1img.setMaximumSize(QtCore.QSize(175, 175))
        self.SID1img.setStyleSheet(GUI_Style.logo)
        self.SID1img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID1img.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SID1img.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SID1img.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SID1img.setAlignment(QtCore.Qt.AlignCenter)
        self.SID1img.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.SID1img.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.SID1img.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.SID1img.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.SID1img.setOptimizationFlags(QtWidgets.QGraphicsView.DontClipPainter)
        self.SID1img.setObjectName("SID1img")

        self.SID1scene = QtWidgets.QGraphicsScene()
        self.SID1scene.addPixmap(QPixmap(SID1_path))
        self.SID1img.setScene(self.SID1scene)
        self.SID1img.fitInView(self.SID1scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

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
        self.SID1_Data.setMaximumWidth(SIDWIDTH)
        self.SID1_Data.setMaximumHeight(50)
      
        # Create Graphics view object to rotate widgets
        self.SID1Data_View = QtWidgets.QGraphicsView()
        self.SID1Data_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID1Data_Scene = QtWidgets.QGraphicsScene(self.SID1Data_View)
        self.SID1Data_View.setScene(self.SID1Data_Scene)
        self.SID1Data_Scene.addWidget(self.SID1_Data)

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        # Add objects to layout
        self.SID1Layout = QtWidgets.QVBoxLayout()
        self.SID1Layout.setSpacing(0)
        self.SID1Layout.setContentsMargins(0, 0, 0, 0) 
        self.SID1Layout.addWidget(self.SID1img)
        self.SID1Layout.addWidget(self.SID1Data_View, 1, Qt.AlignTop)


        # ---------------------------------------------------------------------
        # -------------------- SID 2 Layout -----------------------------------
        # ---------------------------------------------------------------------
        # SID 2 Image
        self.SID2img = QtWidgets.QGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SID2img.sizePolicy().hasHeightForWidth())
        self.SID2img.setSizePolicy(sizePolicy)
        # self.SID1img.setMinimumSize(QtCore.QSize(100, 100))
        self.SID2img.setMaximumSize(QtCore.QSize(175, 175))
        self.SID2img.setStyleSheet(GUI_Style.logo)
        self.SID2img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID2img.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SID2img.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SID2img.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SID2img.setAlignment(QtCore.Qt.AlignCenter)
        self.SID2img.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.SID2img.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.SID2img.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.SID2img.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.SID2img.setOptimizationFlags(QtWidgets.QGraphicsView.DontClipPainter)
        self.SID2img.setObjectName("SID2img")

        self.SID2scene = QtWidgets.QGraphicsScene()
        self.SID2scene.addPixmap(QPixmap(SID2_path))
        self.SID2img.setScene(self.SID2scene)
        self.SID2img.fitInView(self.SID2scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

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
        self.SID2_Data.setMaximumWidth(SIDWIDTH)
        self.SID2_Data.setMaximumHeight(50)


         # Create Graphics view object to rotate widgets
        self.SID2Data_View = QtWidgets.QGraphicsView()
        self.SID2Data_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SID2Data_Scene = QtWidgets.QGraphicsScene(self.SID2Data_View)
        self.SID2Data_View.setScene(self.SID2Data_Scene)
        self.SID2Data_Scene.addWidget(self.SID2_Data)

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        # Add objects to layout
        self.SID2Layout = QtWidgets.QVBoxLayout()
        self.SID2Layout.setSpacing(0)
        self.SID2Layout.setContentsMargins(0, 0, 0, 0)  
        self.SID2Layout.addWidget(self.SID2img)
        self.SID2Layout.addWidget(self.SID2Data_View, 1, Qt.AlignTop)

        # ---------------------------------------------------------------------
        # ----------------- Left Side Button Layout ---------------------------
        # ---------------------------------------------------------------------
        # ----------------------------------
        # ---------- Left Button 1 ---------
        # ----------------------------------
        # Create Left Button 1
        self.leftButton1 = QtWidgets.QPushButton()
        self.leftButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton1.setMinimumSize(60,60)
        self.leftButton1.setIcon(QIcon(LEFT1_ICON))
        self.leftButton1.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.LBtn1_View = QtWidgets.QGraphicsView()
        self.LBtn1_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn1_Scene = QtWidgets.QGraphicsScene(self.LBtn1_View)
        self.LBtn1_View.setScene(self.LBtn1_Scene)
        self.LBtn1_Scene.addWidget(self.leftButton1)

        # ----------------------------------
        # ---------- Left Button 2 ---------
        # ----------------------------------
        # Create Left Button 2
        self.leftButton2 = QtWidgets.QPushButton()
        self.leftButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton2.setMinimumSize(60,60)
        self.leftButton2.setIcon(QIcon(LEFT2_ICON))
        self.leftButton2.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.LBtn2_View = QtWidgets.QGraphicsView()
        self.LBtn2_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn2_Scene = QtWidgets.QGraphicsScene(self.LBtn2_View)
        self.LBtn2_View.setScene(self.LBtn2_Scene)
        self.LBtn2_Scene.addWidget(self.leftButton2)

        # ----------------------------------
        # ---------- Left Button 3 ---------
        # ----------------------------------
        # Create Left Button 3
        self.leftButton3 = QtWidgets.QPushButton()
        self.leftButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton3.setMinimumSize(60,60)
        self.leftButton3.setIcon(QIcon(LEFT3_ICON))
        self.leftButton3.setIconSize(QtCore.QSize(60, 60))
        
        # Create Graphics view object to rotate widgets
        self.LBtn3_View = QtWidgets.QGraphicsView()
        self.LBtn3_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn3_Scene = QtWidgets.QGraphicsScene(self.LBtn3_View)
        self.LBtn3_View.setScene(self.LBtn3_Scene)
        self.LBtn3_Scene.addWidget(self.leftButton3)

        # ----------------------------------
        # ---------- Left Button 4 ---------
        # ----------------------------------
        # Create Left Button 4
        self.leftButton4 = QtWidgets.QPushButton()
        self.leftButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.leftButton4.setMinimumSize(60,60)
        self.leftButton4.setIcon(QIcon(LEFT4_ICON))
        self.leftButton4.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.LBtn4_View = QtWidgets.QGraphicsView()
        self.LBtn4_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBtn4_Scene = QtWidgets.QGraphicsScene(self.LBtn4_View)
        self.LBtn4_View.setScene(self.LBtn4_Scene)
        self.LBtn4_Scene.addWidget(self.leftButton4)

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        self.LeftButtonLayout = QtWidgets.QVBoxLayout()
        self.LeftButtonLayout.setSpacing(25)
        self.LeftButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftButtonLayout.addWidget(self.LBtn1_View, 1, Qt.AlignLeft)
        self.LeftButtonLayout.addWidget(self.LBtn2_View, 1, Qt.AlignLeft)
        self.LeftButtonLayout.addWidget(self.LBtn3_View, 1, Qt.AlignLeft)
        self.LeftButtonLayout.addWidget(self.LBtn4_View, 1, Qt.AlignLeft)

        # --------------------------------------------------------------------
        # ----------------- Gyroscope Layout ---------------------------------
        # --------------------------------------------------------------------
        # ----------------------------------
        # -------- Gyroscope x-axis --------
        # ----------------------------------
        # Create X Axis label
        self.xGyro = QLabel()
        self.xGyro.setMinimumSize(60, 12)
        self.xGyro.setStyleSheet(GUI_Style.statusBar_widgets)
        self.xGyro.setText("x-gyro")
        # self.xAxis.setAlignment(Qt.AlignCenter)

        # Create Graphics view object to rotate widgets
        self.xG_View = QtWidgets.QGraphicsView()
        self.xG_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.xG_Scene = QtWidgets.QGraphicsScene(self.xG_View)
        self.xG_View.setScene(self.xG_Scene)
        self.xG_Scene.addWidget(self.xGyro)
        
        # ----------------------------------
        # -------- Gyroscope y-axis --------
        # ----------------------------------
        # Create Y Axis label
        self.yGyro = QLabel()
        self.yGyro.setMinimumSize(60, 12)
        self.yGyro.setStyleSheet(GUI_Style.statusBar_widgets)
        self.yGyro.setText("y-gyro")
        # self.yAxis.setAlignment(Qt.AlignCenter)
        
        # Create Graphics view object to rotate widgets
        self.yG_View = QtWidgets.QGraphicsView()
        self.yG_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yG_Scene = QtWidgets.QGraphicsScene(self.yG_View)
        self.yG_View.setScene(self.yG_Scene)
        self.yG_Scene.addWidget(self.yGyro)

        # ----------------------------------
        # -------- Gyroscope z-axis --------
        # ----------------------------------
        # Create Z Axis label
        self.zGyro = QLabel()
        self.zGyro.setMinimumSize(60, 15)
        self.zGyro.setStyleSheet(GUI_Style.statusBar_widgets)
        self.zGyro.setText("z-gyro")
        # self.zAxis.setAlignment(Qt.AlignCenter)

        # Create Graphics view object to rotate widgets
        self.zG_View = QtWidgets.QGraphicsView()
        self.zG_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.zG_Scene = QtWidgets.QGraphicsScene(self.zG_View)
        self.zG_View.setScene(self.zG_Scene)
        self.zG_Scene.addWidget(self.zGyro)

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        self.Gyroscope = QtWidgets.QGroupBox("Gyroscope")
        VGylayout = QtWidgets.QVBoxLayout()
        VGylayout.addWidget(self.xG_View)
        VGylayout.addWidget(self.yG_View)
        VGylayout.addWidget(self.zG_View)
        VGylayout.setSpacing(5)
        VGylayout.setContentsMargins(0, 0, 0, 0)

        self.Gyroscope.setLayout(VGylayout)
        self.Gyroscope.setStyleSheet(GUI_Style.groupBox)
        self.Gyroscope.setMaximumSize(200, 150)
        # ~ self.Gyroscope.setMinimumSize(100, 100)

        # ---------------------------------------------------------------------
        # ----------------- Accelerometer Layout ------------------------------
        # ---------------------------------------------------------------------
        # ----------------------------------
        # ------ Acceleromter X-Axis ------- 
        # ----------------------------------

        # Create X Axis label
        self.xAxis = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxis.sizePolicy().hasHeightForWidth())
        self.xAxis.setSizePolicy(sizePolicy)
        self.xAxis.setStyleSheet(GUI_Style.SID_Data)
        self.xAxis.setScaledContents(True)
        self.xAxis.setAlignment(QtCore.Qt.AlignCenter)
        self.xAxis.setText("\N{DEGREE SIGN}")
        # self.xAxis.setMaximumSize(120,50)
        self.xAxis.setMaximumWidth(140)
        self.xAxis.setMaximumHeight(50)

        # Create Graphics view object to rotate widgets
        self.xAx_View = QtWidgets.QGraphicsView()
        self.xAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.xAx_Scene = QtWidgets.QGraphicsScene(self.xAx_View)
        self.xAx_View.setScene(self.xAx_Scene)
        self.xAx_Scene.addWidget(self.xAxis)
        
        # ----------------------------------
        # ------ Acceleromter Y-Axis -------
        # ----------------------------------
        # Create Y Axis label
        self.yAxis = QLabel()
        self.yAxis.setMinimumSize(60, 12)
        self.yAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.yAxis.setText("y-axis")
        # self.yAxis.setAlignment(Qt.AlignCenter)
        
        # Create Graphics view object to rotate widgets
        self.yAx_View = QtWidgets.QGraphicsView()
        self.yAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yAx_Scene = QtWidgets.QGraphicsScene(self.yAx_View)
        self.yAx_View.setScene(self.yAx_Scene)
        self.yAx_Scene.addWidget(self.yAxis)

        # ----------------------------------
        # ------ Acceleromter Z-Axis -------
        # ----------------------------------
        # Create Z Axis label
        self.zAxis = QLabel()
        self.zAxis.setMinimumSize(60, 15)
        self.zAxis.setStyleSheet(GUI_Style.statusBar_widgets)
        self.zAxis.setText("z-axis")
        # self.zAxis.setAlignment(Qt.AlignCenter)

        # Create Graphics view object to rotate widgets
        self.zAx_View = QtWidgets.QGraphicsView()
        self.zAx_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.zAx_Scene = QtWidgets.QGraphicsScene(self.zAx_View)
        self.zAx_View.setScene(self.zAx_Scene)
        self.zAx_Scene.addWidget(self.zAxis)


        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        self.AcelLayout = QtWidgets.QVBoxLayout()
        self.AcelLayout.setSpacing(0)
        self.AcelLayout.setContentsMargins(0, 0, 0, 0)


        # ---------------------------------------------------------------------
        # ----------------- Right Side Button Layout --------------------------
        # ---------------------------------------------------------------------
        # ----------------------------------
        # ---------- Right Button 1 --------
        # ----------------------------------
        # Create Right Button 1
        self.rightButton1 = QtWidgets.QPushButton()
        self.rightButton1.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton1.setMinimumSize(60,60)
        self.rightButton1.setIcon(QIcon(RIGHT1_ICON))
        self.rightButton1.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.RBtn1_View = QtWidgets.QGraphicsView()
        self.RBtn1_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn1_Scene = QtWidgets.QGraphicsScene(self.RBtn1_View)
        self.RBtn1_View.setScene(self.RBtn1_Scene)
        self.RBtn1_Scene.addWidget(self.rightButton1)

        # ----------------------------------
        # ---------- Right Button 2 --------
        # ----------------------------------
        # Create Right Button 2
        self.rightButton2 = QtWidgets.QPushButton()
        self.rightButton2.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton2.setMinimumSize(60,60)
        self.rightButton2.setIcon(QIcon(RIGHT2_ICON))
        self.rightButton2.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.RBtn2_View = QtWidgets.QGraphicsView()
        self.RBtn2_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn2_Scene = QtWidgets.QGraphicsScene(self.RBtn2_View)
        self.RBtn2_View.setScene(self.RBtn2_Scene)
        self.RBtn2_Scene.addWidget(self.rightButton2)

        # ----------------------------------
        # ---------- Right Button 3 --------
        # ----------------------------------
        # Create Right Button 3
        self.rightButton3 = QtWidgets.QPushButton()
        self.rightButton3.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton3.setMinimumSize(60,60)
        self.rightButton3.setIcon(QIcon(RIGHT3_ICON))
        self.rightButton3.setIconSize(QtCore.QSize(60, 60))
        
        # Create Graphics view object to rotate widgets
        self.RBtn3_View = QtWidgets.QGraphicsView()
        self.RBtn3_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn3_Scene = QtWidgets.QGraphicsScene(self.RBtn3_View)
        self.RBtn3_View.setScene(self.RBtn3_Scene)
        self.RBtn3_Scene.addWidget(self.rightButton3)

        # ----------------------------------
        # ---------- Right Button 4 --------
        # ----------------------------------
        # Create Right Button 4
        self.rightButton4 = QtWidgets.QPushButton()
        self.rightButton4.setStyleSheet(GUI_Style.buttonIdle)
        self.rightButton4.setMinimumSize(60,60)
        self.rightButton4.setIcon(QIcon(RIGHT4_ICON))
        self.rightButton4.setIconSize(QtCore.QSize(60, 60))

        # Create Graphics view object to rotate widgets
        self.RBtn4_View = QtWidgets.QGraphicsView()
        self.RBtn4_View.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RBtn4_Scene = QtWidgets.QGraphicsScene(self.RBtn4_View)
        self.RBtn4_View.setScene(self.RBtn4_Scene)
        self.RBtn4_Scene.addWidget(self.rightButton4)

        # ----------------------------------
        # ---- Add Objects to layout -------
        # ----------------------------------
        #  Add Objects to right button layout
        self.RightButtonLayout = QtWidgets.QVBoxLayout()
        self.RightButtonLayout.setSpacing(25)
        self.RightButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.RightButtonLayout.addWidget(self.RBtn1_View, 1, Qt.AlignRight)
        self.RightButtonLayout.addWidget(self.RBtn2_View, 1, Qt.AlignRight)
        self.RightButtonLayout.addWidget(self.RBtn3_View, 1, Qt.AlignRight)
        self.RightButtonLayout.addWidget(self.RBtn4_View, 1, Qt.AlignRight)

        # ---------------------------------------------------------------------
        # ----------------- Bottom Horizontal Layout --------------------------
        # ---------------------------------------------------------------------
        self.rightLogoLayout = QtWidgets.QVBoxLayout()
        self.leftLogoLayout = QtWidgets.QVBoxLayout()
        self.rightHeaderLayout = QtWidgets.QVBoxLayout()
        self.leftHeaderLayout = QtWidgets.QVBoxLayout()



        self.BottomLayout = QtWidgets.QHBoxLayout()
        self.BottomLayout.setSpacing(20)
        self.BottomLayout.setContentsMargins(0, 0, 0, 0)
        self.BottomLayout.addLayout(self.LeftButtonLayout)
        self.BottomLayout.addLayout(self.leftLogoLayout)
        self.BottomLayout.addLayout(self.leftHeaderLayout)
        self.BottomLayout.addLayout(self.SID1Layout)
        self.BottomLayout.addLayout(self.SID2Layout)
        self.BottomLayout.addLayout(self.AcelLayout)
        self.BottomLayout.addLayout(self.rightHeaderLayout)
        self.BottomLayout.addLayout(self.rightLogoLayout)

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
        self.SID2_Data.setText(_translate("MainWindow", "1000"))
        self.SID1_Data.setText(_translate("MainWindow", "1000"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


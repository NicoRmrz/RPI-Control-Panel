from PyQt5.QtCore import QObject



# --------------------------------------------------------------------------------------------------------------
# --------------------------------- GUI setStylesheet Class ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------- 
class GUI_Stylesheets(QObject):
	
	 # Initializes the necessary objects into the slider class for control
	def __init__(self):
		super(GUI_Stylesheets, self).__init__()
		


		# ~ self.mainWidget = ("background-color: rgb(119, 136, 153);")	
		self.mainWidget = ("background-color: #05090C;")	

		self.timer = ("font: 14pt \"Arial\";\n"
						"color: rgb(255, 255, 255);\n"
						"background-color: rgba(255, 255, 255, 0);")


		self.logo = ("background-color: rgba(255, 255, 255, 0);\n"
						"selection-color: rgba(255, 255, 255, 0);\n"
						"color: rgba(255, 255, 255, 0);\n"
						"alternate-background-color: rgba(255, 255, 255, 0);\n"
						"gridline-color: rgba(255, 255, 255, 0);\n"
						"border-color: rgba(255, 255, 255, 0);")

		self.statusBarWhite = ("QStatusBar { background: rgb(58, 213, 255); "
										"color:white;} "

							"QStatusBar::item {border: 1px solid rgba(242,242,242, 0); "
								"border-radius: 3px; "
								"background-color: rgba(242,242,242, 0)}"
							)
		
		
							
		self.statusBar_XY	= (	"QLabel {border: none; "
								"background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
								"stop:0 rgba(242, 242, 242, 0), "
								"stop:1 rgba(242,242,242, 0)); "						
								"font: 40 px; "
								"font-weight: bold; "
								"color: white; }"			
							)			
							
		
							
		self.statusBar_widgets	= (	"QLabel {border: none; "
								"background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
								"stop:0 rgba(242, 242, 242, 0), "
								"stop:1 rgba(242,242,242, 0)); "						
								"font: 20 px; "
								"font-weight: bold; "
								"color: white; }"			
							)			
							
		self.SID = ("color: rgb(255, 255, 255);\n"
						"background-color: rgba(255, 255, 255, 0);\n"
						"font: 18pt \"Arial\";")

		self.SID_Data = ("font: 32pt \"Arial\";\n"
						"color: rgb(255, 255, 255);\n"
						"background-color: rgba(255, 255, 255, 0); border: none;")

		self.groupBox = ("font: bold 11px Verdana; "
	                    "color: white; "
	                    "background-color: rgba(18,151,147,0);"
	                    )


		self.buttonIdle = ("font: bold 12px Verdana; "
                           "background-color: #6d6e70; "
                           # ~ "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
                                # ~ "stop:0 rgba(88, 139, 174, 240), "
                                # ~ "stop:1 rgba(255,255,255,255)); "
                           "border-style: outset; "
                           "border-radius: 9px; "
                           "border-width: 1px; "
                           "border-color: #6d6e70; "
                           # ~ "border: none; "
			   				"color: white; "
                           "padding: 4px;"
                           )
			   
		self.buttonPressed = ("font: bold 12px Verdana; "
							  "background-color: rgba(72,146,73,240); "
							  "border-style: outset; "
							  "border-radius: 9px; "
							  "border-width: 1px; "
							  "border-color: rgba(72,146,73,240); "
							  "padding: 4px;"
							  )
			   
		self.exitBtn = ("font: bold 12px Verdana; "
							  "background-color: qlineargradient(spread:pad x1:0.45, y1:0.3695, x2:0.427, y2:0, "
							  "stop:0 rgba(202, 51, 52, 0), "
							  "stop:1 rgba(255,255,255,0)); "
							  "border: none; "
							  )

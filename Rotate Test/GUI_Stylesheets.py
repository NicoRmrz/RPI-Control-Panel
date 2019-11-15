from PyQt5.QtCore import QObject

# --------------------------------------------------------------------------------------------------------------
# --------------------------------- GUI setStylesheet Class ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------- 
class GUI_Stylesheets(QObject):
	
	 # Initializes the necessary objects into the slider class for control
	def __init__(self):
		super(GUI_Stylesheets, self).__init__()
		


		self.mainWidget = ("background-color: rgb(119, 136, 153);")	

		self.timer = ("font: 14pt \"Arial\";\n"
						"color: rgb(255, 255, 255);\n"
						"background-color: rgba(255, 255, 255, 0);")


		self.logo = ("background-color: rgba(255, 255, 255, 0);\n"
						"selection-color: rgba(255, 255, 255, 0);\n"
						"color: rgba(255, 255, 255, 0);\n"
						"alternate-background-color: rgba(255, 255, 255, 0);\n"
						"gridline-color: rgba(255, 255, 255, 0);\n"
						"border-color: rgba(255, 255, 255, 0);")

		self.exitBtn = ("background-color: rgba(255,255,255,0);\n"
							"border-color: rgba(255, 255, 255, 0);\n"
							# "background-image: url(icons/Button-Close-icon x 64.png)\n"
							"")
		
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
								"font: 20 px; "
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
						"font: 24pt \"Arial\";")

		self.SID_Data = ("font: 36pt \"Arial\";\n"
						"color: rgb(255, 255, 255);\n"
						"background-color: rgba(255, 255, 255, 0); border: none;")

		self.groupBox = ("font: bold 11px Verdana; "
	                    "color: white; "
	                    "background-color: rgba(18,151,147,0);"
	                    )
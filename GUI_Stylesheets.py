from PyQt5.QtCore import QObject

# --------------------------------------------------------------------------------------------------------------
# --------------------------------- GUI setStylesheet Class ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------- 
class GUI_Stylesheets(QObject):
	
	 # Initializes the necessary objects into the slider class for control
	def __init__(self):
		super(GUI_Stylesheets, self).__init__()
		
		
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
							
		

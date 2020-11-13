from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow
from PyQt5.QtCore import Qt

if __name__== "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    ui = MainWindow()
    ui.showFullScreen()
    # ~ ui.show()
    sys.exit(app.exec_())
    

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import silnik

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wyszukiwarka Projektów")
    
        label = QLabel("Wyszukaj Projekt:")
        label.setAlignment(Qt.AlignLeft)
        self.setCentralWidget(label)

        toolbar = QToolBar("Pasek Narzędzi")
        self.addToolBar(toolbar)

        elemList = QListWidget()
        #elemList.setAlignment(Qt.AlignTop)
        self.setCentralWidget(elemList)

        button = QAction("Kliknij", self)
        button.setStatusTip("Kliknij ten przycisk")
        button.triggered.connect(self.clickedButton)
        toolbar.addAction(button)

        self.setStatusBar(QStatusBar(self))

    def clickedButton(self, s):
        print("Klinknąłeś!", s)

    def openFolder(self, o):
        webbrowser.open(silnik.Engine.path_)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
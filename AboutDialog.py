import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QSizePolicy, QSpacerItem, QMainWindow

class AboutDialog(QMainWindow):
    infoFilePath = "README.md"
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("ReadMe")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        vBoxLayout = QVBoxLayout(centralWidget)

        self.infoLabel = QLabel(self)
        vBoxLayout.addWidget(self.infoLabel)
        self.infoLabel.setText("No info file founded =(")

        spacerItem = QSpacerItem(0,0,QSizePolicy.Expanding, QSizePolicy.Expanding)

        vBoxLayout.addSpacerItem(spacerItem)

        self.okPushButton = QPushButton(self)
        self.okPushButton.setText("Ok")
        vBoxLayout.addWidget(self.okPushButton)
        self.okPushButton.clicked.connect(self.close)

        self.readInfoFile()

    def readInfoFile(self):
        if not os.path.isfile(self.infoFilePath):
            return

        fileDescr = open(self.infoFilePath, 'r')
        if fileDescr.readable():
            fileData = fileDescr.read()
            self.infoLabel.setText(fileData)

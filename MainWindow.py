import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMenuBar
from AboutDialog import AboutDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.showMaximized()
        self.setWindowTitle("Image Filter 0.1")
        self.initMainMenu()

    def initMainMenu(self):
        mainMenu = QMenuBar(self)
        self.setMenuBar(mainMenu)

        fileMenu = mainMenu.addMenu("&File")
        aboutMenu = mainMenu.addMenu("&About")

        aboutDialogAction = aboutMenu.addAction("Readme")
        aboutDialogAction.triggered.connect(self.showAboutDialog)

    def showAboutDialog(self, e):
        aboutDialog = AboutDialog(self)
        aboutDialog.show()

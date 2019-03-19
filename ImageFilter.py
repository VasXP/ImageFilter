import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QMainWindow

from MainWindow import MainWindow

class ImageFilter(QObject):
    def __init__(self, parent=None):
        super(ImageFilter, self).__init__(parent)
        self.mainWindow = MainWindow()

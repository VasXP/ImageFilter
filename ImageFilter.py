import sys
from PyQt5.QtCore import Qt, QObject, QDir
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from MainWindow import MainWindow
from AboutDialog import AboutDialog

class ImageFilter(QObject):
    def __init__(self, parent=None):
        super(ImageFilter, self).__init__(parent)
        self.mainWindow = MainWindow()
        self.initConnects()

    def initConnects(self):
        self.mainWindow.openImageRequest.connect(self.openImage)
        self.mainWindow.showAboutDialogRequest.connect(self.showAboutDialog)
        self.mainWindow.saveImageRequest.connect(self.saveImage)
        self.mainWindow.saveAsImageRequest.connect(self.saveAsImage)

    def showAboutDialog(self):
        aboutDialog = AboutDialog(self.mainWindow)
        aboutDialog.show()

    def openImage(self):
        self.fileName = QFileDialog.getOpenFileName(self.mainWindow, "Open image", QDir.currentPath(), "Images (*.png *.xpm *.jpg)")[0]
        if not self.fileName:
            return

        self.image = QImage(self.fileName)
        self.mainWindow.setImage(self.image)

    def saveImage(self):
        try:
            self.image
        except:
            return

        rw = QMessageBox.question(self.mainWindow, "Rewriting old image", "Rewrite old image? ", QMessageBox.Yes, QMessageBox.No)
        if (rw == QMessageBox.Yes):
            self.image.save(self.fileName)

    def saveAsImage(self):
        try:
            self.image
        except:
            return

        self.fileName = QFileDialog.getSaveFileName(self.mainWindow, "Save image as", QDir.currentPath(), "Images (*.png *.xpm *.jpg)")[0]
        print(self.fileName)
        if not self.fileName:
            return

        self.image.save(self.fileName)

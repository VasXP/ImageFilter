import sys
import os
from PyQt5.QtCore import Qt, QObject, QDir, QUuid
from PyQt5.QtGui import QImage, QMovie
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QLabel

from MainWindow import MainWindow
from AboutDialog import AboutDialog
from FastNlMeansDenoisingDialog import FastNlMeansDenoisingDialog
from FiltrationHandler import FiltrationHandler 

class ImageFilter(QObject):
    images = {}
    imageNames = {}
    imageOrders = []

    def __init__(self, parent=None):
        super(ImageFilter, self).__init__(parent)
        self.mainWindow = MainWindow()
        self.initConnects()

        self.filtrationHandler = FiltrationHandler(self)
        self.filtrationHandler.addResultRequest.connect(self.addFiltredImage)
        self.filtrationHandler.startOperation.connect(self.startOperation)
        self.filtrationHandler.stopOperation.connect(self.stopOperation)
        

    def initConnects(self):
        self.mainWindow.openImageRequest.connect(self.openImage)
        self.mainWindow.showAboutDialogRequest.connect(self.showAboutDialog)
        self.mainWindow.saveImageRequest.connect(self.saveImage)
        self.mainWindow.saveAsImageRequest.connect(self.saveAsImage)
        self.mainWindow.useFastNlMeansDenoisingRequest.connect(self.showFastNlMeansDenoisingDialog)
        self.mainWindow.updateImage.connect(self.updateShowImage)

    def showAboutDialog(self):
        aboutDialog = AboutDialog(self.mainWindow)
        aboutDialog.show()

    def openImage(self):
        self.fileName = QFileDialog.getOpenFileName(self.mainWindow, "Open image", QDir.currentPath(), "Images (*.png *.xpm *.jpg)")[0]
        if not self.fileName:
            return

        image = QImage(self.fileName)
        imageName = self.fileName.split(os.sep)[-1]
        
        path = QUuid.createUuid().toString()
        self.images[path] = image
        self.imageNames[path] = imageName
        self.imageOrders.append(path)

        self.mainWindow.setImages(self.imageNames, self.imageOrders)

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

    def showFastNlMeansDenoisingDialog(self):
        dialog = FastNlMeansDenoisingDialog(self.mainWindow)
        dialog.setImages(self.imageNames)
        dialog.show()
        dialog.startCalc.connect(self.startFastNlDenoisingFiltration)

    def startFastNlDenoisingFiltration(self, path, name, h, tWS, sWS):
        image = self.images[path]
        self.filtrationHandler.startFastNlMeansFiltration(image, name, h, tWS, sWS)
    
    def addFiltredImage(self, image, name):
        path = QUuid.createUuid().toString()
        self.images[path] = image
        self.imageNames[path] = name
        self.imageOrders.append(path)
        self.mainWindow.setImages(self.imageNames, self.imageOrders)

    def updateShowImage(self, box, index):
        if index < 0 or index >= len(self.imageOrders):
            return

        path = self.imageOrders[index]
        image = self.images[path]
        self.mainWindow.setImage(box, image)

    def startOperation(self):
        self.waitLabel = QLabel(self.mainWindow)
        self.waitLabel.setWindowFlags(Qt.Window)
        self.waitLabel.setGeometry(self.mainWindow.x() + self.mainWindow.width()/2 - 50, self.mainWindow.y() + self.mainWindow.height()/2 - 50, 100, 100)
        self.waitMovie = QMovie("loader.gif")
        self.waitLabel.setMovie(self.waitMovie)
        self.waitLabel.setWindowModality(Qt.WindowModal)
        self.waitLabel.show()
        self.waitMovie.start()

    def stopOperation(self):
        self.waitLabel.deleteLater()
        self.waitMovie.deleteLater()


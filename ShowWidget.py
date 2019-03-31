import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QWidget, QGroupBox, QComboBox
from ImageViewWidget import ImageViewWidget

class ShowWidget(QWidget):
    updateImage = pyqtSignal(int, int)
    def __init__(self, parent=None):
        super(ShowWidget, self).__init__(parent)
        self.initUI()


    def initUI(self):
        # first group box for image
        oldImageBox = QGroupBox()
        oldImageBox.setTitle("Image before...")
        
        # layout for image and combobox
        oldVLayout = QVBoxLayout()
        oldImageBox.setLayout(oldVLayout)

        oldHComboLayout = QHBoxLayout()
        oldVLayout.addLayout(oldHComboLayout)

        self.oldImageComboBox = QComboBox(self)
        oldHComboLayout.addWidget(self.oldImageComboBox)
        self.oldImageComboBox.currentIndexChanged[int].connect(self.updateOldImage)

        self.oldImageView = ImageViewWidget(self)
        oldVLayout.addWidget(self.oldImageView)
        
        oldSpacerItem = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        oldHComboLayout.addItem(oldSpacerItem)


        newImageBox = QGroupBox()
        newImageBox.setTitle("Image after...")
        
        newVLayout = QVBoxLayout()
        newImageBox.setLayout(newVLayout)

        newHComboLayout = QHBoxLayout()
        newVLayout.addLayout(newHComboLayout)

        self.newImageComboBox = QComboBox(self)
        newHComboLayout.addWidget(self.newImageComboBox)
        self.newImageComboBox.currentIndexChanged[int].connect(self.updateNewImage)

        self.newImageView = ImageViewWidget(self)
        newVLayout.addWidget(self.newImageView)
        
        newSpacerItem = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        newHComboLayout.addItem(newSpacerItem)

        hLayout = QHBoxLayout(self)
        
        hLayout.addWidget(oldImageBox)
        hLayout.addWidget(newImageBox)

        self.setLayout(hLayout)
    
    def setImages(self, imageNames, imageOrders):
        self.oldImageComboBox.clear()
        self.newImageComboBox.clear()

        oldImageIndex = self.oldImageComboBox.currentIndex()
        newImageIndex = self.newImageComboBox.currentIndex()

        self.oldImageComboBox.blockSignals(True)
        self.newImageComboBox.blockSignals(True)

        for path in imageOrders:
            name = imageNames[path]
            self.oldImageComboBox.addItem(name, path)
            self.newImageComboBox.addItem(name, path)

        self.oldImageComboBox.blockSignals(False)
        self.newImageComboBox.blockSignals(False)

        if oldImageIndex == -1:
            self.updateImage.emit(0, 0)

        if newImageIndex == -1:
            self.updateImage.emit(1, 0)

    def setImage(self, box, image):
        if box == 0:
            self.oldImageView.setImage(image)

        if box == 1:
            self.newImageView.setImage(image)

    def updateOldImage(self, index):
        self.updateImage.emit(0, index)

    def updateNewImage(self, index):
        self.updateImage.emit(1, index)

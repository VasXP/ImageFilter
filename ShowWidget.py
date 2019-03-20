import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QWidget, QGroupBox
from ImageViewWidget import ImageViewWidget

class ShowWidget(QWidget):
    def __init__(self, parent=None):
        super(ShowWidget, self).__init__(parent)
        self.initUI()


    def initUI(self):
        oldImageBox = QGroupBox(self)
        oldImageBox.setTitle("Image before...")
        
        oldHLayout = QHBoxLayout()
        oldImageBox.setLayout(oldHLayout)

        self.oldImageView = ImageViewWidget(self)
        oldHLayout.addWidget(self.oldImageView)


        newImageBox = QGroupBox(self)
        newImageBox.setTitle("Image after...")
        
        newHLayout = QHBoxLayout()
        newImageBox.setLayout(newHLayout)

        self.newImageView = ImageViewWidget(self)
        newHLayout.addWidget(self.newImageView)

        hLayout = QHBoxLayout()
        
        hLayout.addWidget(oldImageBox)
        hLayout.addWidget(newImageBox)

        self.setLayout(hLayout)
    
    def setImage(self, image):
        self.newImageView.setImage(image)
        self.oldImageView.setImage(image)

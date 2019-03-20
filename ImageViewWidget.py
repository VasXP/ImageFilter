import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QImage
from PyQt5.QtWidgets import QWidget

class ImageViewWidget(QWidget):
    drawImage = QImage()
    scaleX = 1.0
    scaleY = 1.0
    translateX = 0
    translateY = 0
    oldX = 0
    oldY = 0

    def __init__(self, parent=None):
        super(ImageViewWidget, self).__init__(parent)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)

        oldWidth = self.drawImage.width()
        oldHeight = self.drawImage.height()
        if oldWidth == 0 or oldHeight == 0:
            return

        newCoords = QPoint(self.translateX, self.translateY)

        copyImage = self.drawImage.scaled(oldWidth*self.scaleX, oldHeight*self.scaleY)
        painter.drawImage(newCoords, copyImage)
        painter.end()
    def mousePressEvent(self, event):
        self.oldX = event.pos().x()
        self.oldY = event.pos().y()

    def mouseMoveEvent (self, event):
        point = event.pos() - QPoint(self.oldX, self.oldY)
        mb = event.buttons()
        if (mb and Qt.LeftButton):
            self.translateX += point.x()
            self.translateY += point.y()
            self.oldX = event.pos().x()
            self.oldY = event.pos().y()

            self.repaint()
    def wheelEvent(self,event):
        if (event.angleDelta().y() > 0):
            if (self.scaleX > 10 or self.scaleY > 10):
                return

            self.scaleX *= 1.2
            self.scaleY *= 1.2

        if (event.angleDelta().y() < 0):
            if (self.scaleX < 1/20 or self.scaleY < 1/20):
                return

            self.scaleX /= 1.2
            self.scaleY /= 1.2
        self.repaint()

    def setImage(self, image):
        self.drawImage = image
        self.repaint()

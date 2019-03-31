import sys
import numpy as np
import cv2
import time

from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage

class FiltrationThread(QObject):
    start = pyqtSignal()
    filtrationEnded = pyqtSignal(QImage, str)
    finished = pyqtSignal()
    error = pyqtSignal()
    startOperation = pyqtSignal()
    stopOperation = pyqtSignal()

    def __init__(self, parent=None):
        super(FiltrationThread, self).__init__(parent)

    def setData(self, image, resName, h, tWS, sWS):
        self.image = image
        self.resName = resName
        self.h = h
        self.tWS = tWS
        self.sWS = sWS

    def calculate(self):
        self.startOperation.emit()

        # QImage to cv2
        cv2Arr = self.QImageToCV2(self.image)

        # Calculation
        result = cv2.fastNlMeansDenoising(cv2Arr, None, self.h, self.tWS, self.sWS)

        # cv2 to QImage
        resultImage = self.CV2ToQImage(result, True)

        self.stopOperation.emit()
        self.filtrationEnded.emit(resultImage, self.resName)
        self.finished.emit()

    def QImageToCV2(self, qimg):
        qimg.convertToFormat(QImage.Format.Format_RGB32)
        #qimg = qimg.rgbSwapped()
        
        width = qimg.width()
        height = qimg.height()

        buf = qimg.bits().asstring(qimg.width() * qimg.height() * 4)
        arr = np.fromstring(buf, dtype=np.uint8).reshape((qimg.height(), qimg.width(), 4))
        return arr

    def CV2ToQImage(self, im, copy=False):
        if im is None:
            return QImage()

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888);
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32);
                    return qim.copy() if copy else qim

        raise NotImplementedException

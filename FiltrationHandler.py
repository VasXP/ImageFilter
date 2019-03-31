import sys
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage

from FiltrationThread import FiltrationThread

class FiltrationHandler(QObject):
    addResultRequest = pyqtSignal(QImage, str)
    startOperation = pyqtSignal()
    stopOperation = pyqtSignal()

    def __init__(self, parent=None):
        super(FiltrationHandler, self).__init__(parent)

    def startFastNlMeansFiltration(self, image, resName, h, tWS, sWS):
        self.fThread = FiltrationThread()
        self.fThread.setData(image, resName, h, tWS, sWS)

        self.thread = QThread()
        self.thread.start()

        self.fThread.finished.connect(self.fThread.deleteLater)
        self.fThread.finished.connect(self.thread.quit)
        self.fThread.finished.connect(self.thread.deleteLater)
        self.fThread.error.connect(self.thread.quit)
        self.fThread.error.connect(self.thread.deleteLater)

        self.fThread.moveToThread(self.thread)

        self.fThread.filtrationEnded.connect(self.addResultRequest)
        self.fThread.start.connect(self.fThread.calculate)
        
        self.fThread.startOperation.connect(self.startOperation)
        self.fThread.stopOperation.connect(self.stopOperation)
        
        self.fThread.start.emit()
        #self.thread = QThread()

        #self.fThread.finished.connect(self.fThread.deleteLater)
        #self.fThread.finished.connect(self.thread.quit)
        #self.fThread.finished.connect(self.thread.deleteLater)
        #self.fThread.error.connect(self.thread.quit)
        #self.fThread.error.connect(self.thread.deleteLater)

        #self.fThread.filtrationEnded.connect(self.addResultRequest)
        #self.thread.started.connect(self.fThread.calculate)
        
        #self.fThread.startOperation.connect(self.startOperation)
        #self.fThread.stopOperation.connect(self.stopOperation)
        
        #self.fThread.moveToThread(self.thread)
        #self.thread.start()

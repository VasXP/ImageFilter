import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QAction
from PyQt5.QtGui import QKeySequence
from ShowWidget import ShowWidget

class MainWindow(QMainWindow):
    openImageRequest = pyqtSignal()
    saveImageRequest = pyqtSignal()
    saveAsImageRequest = pyqtSignal()
    useFastNlMeansDenoisingRequest = pyqtSignal()
    useSecondFilterRequest = pyqtSignal()
    showAboutDialogRequest = pyqtSignal()
    updateImage = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.showMaximized()
        self.setWindowTitle("Image Filter 0.1")
        self.initMainMenu()
        self.initCentralWidget()
    
    def initMainMenu(self):
        # Menu decloration
        mainMenu = QMenuBar(self)
        self.setMenuBar(mainMenu)
        # File menu
        fileMenu = mainMenu.addMenu("&File")

        # --> Open image action
        openAction  = fileMenu.addAction("Open image")
        openAction.triggered.connect(self.openImageRequest)
        openAction.setShortcuts(QKeySequence.Open)

        # --> Save image action
        saveAction  = fileMenu.addAction("Save image")
        saveAction.triggered.connect(self.saveImageRequest)
        saveAction.setShortcuts(QKeySequence.Save)

        # --> Save As image action
        saveAsAction  = fileMenu.addAction("Save image As ...")
        saveAsAction.triggered.connect(self.saveAsImageRequest)
        saveAsAction.setShortcuts(QKeySequence.SaveAs)

        # Filter menu
        filterMenu = mainMenu.addMenu("Fil&ter")

        # --> OpenCV filters
        opencvFiltersMenu = filterMenu.addMenu("OpenCV filters")

        # --> --> FastNlMeansDenoising
        fastNlMeansDenoisingAction = opencvFiltersMenu.addAction("FastNlMeansDenoising filter")
        fastNlMeansDenoisingAction.triggered.connect(self.useFastNlMeansDenoisingRequest)
        fastNlMeansDenoisingAction.setShortcuts(QKeySequence("Ctrl+1"))

        # --> --> Erode
        #erodeFilterAction = opencvFilterMenu.addAction("Erode filter")
        #erodeFilterAction.triggered.connect(self.useErodeFilterRequest)

        # --> Second filter
        secondFilterAction = filterMenu.addAction("Second filter")
        secondFilterAction.triggered.connect(self.useSecondFilterRequest)

        # About menu
        aboutMenu = mainMenu.addMenu("&About")

        # --> readme
        aboutDialogAction = aboutMenu.addAction("Readme")
        aboutDialogAction.triggered.connect(self.showAboutDialogRequest)

    def initCentralWidget(self):
        self.centrWidget = ShowWidget(self)
        self.setCentralWidget(self.centrWidget)
        self.centrWidget.updateImage.connect(self.updateImage)

    def setImages(self, imageNames, imageOrders):
        self.centrWidget.setImages(imageNames, imageOrders)

    def setImage(self, box, image):
        self.centrWidget.setImage(box, image)

import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtWidgets import QMainWindow, QComboBox, QFormLayout, QLineEdit, QSlider, QSpinBox

class FastNlMeansDenoisingDialog(QMainWindow):
    startCalc = pyqtSignal(str, str, int, int, int)
    def __init__(self, parent=None):
        super(FastNlMeansDenoisingDialog, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Filter settings")
        
        # Весь виджет
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Лайоут общий
        vBoxLayout = QVBoxLayout()
        centralWidget.setLayout(vBoxLayout)

        formLayout = QFormLayout()
        vBoxLayout.addLayout(formLayout)
        # Комбобокс выбора картинки
        self.imageComboBox = QComboBox(self)
        formLayout.addRow("Image:", self.imageComboBox)

        # Имя для новой картинки
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setText("name")
        formLayout.addRow("Name:", self.nameLineEdit)
        
        # Параметр h
        self.hParamSlider = QSlider(Qt.Horizontal, self)
        self.hParamSlider.setMinimum(0)
        self.hParamSlider.setMaximum(100)
        self.hParamSlider.setValue(20)
        formLayout.addRow("H [0,100]:", self.hParamSlider)

        # Параметр tWS
        self.tWSSpinBox = QSpinBox(self)
        self.tWSSpinBox.setMinimum(0)
        self.tWSSpinBox.setMaximum(100)
        self.tWSSpinBox.setValue(7)
        formLayout.addRow("tWS:", self.tWSSpinBox)

        # Параметр sWS
        self.sWSSpinBox = QSpinBox(self)
        self.sWSSpinBox.setMinimum(0)
        self.sWSSpinBox.setMaximum(100)
        self.sWSSpinBox.setValue(21)
        formLayout.addRow("sWS:", self.sWSSpinBox)

        # Кнопка запуска расчёта
        self.startPushButton = QPushButton(self)
        self.startPushButton.setText("Start")
        self.startPushButton.clicked.connect(self.calcRequested)
        vBoxLayout.addWidget(self.startPushButton)

    def setImages(self, paths):
        for key, value in paths.items():
            self.imageComboBox.addItem(value, key)


    def calcRequested(self):
        if self.imageComboBox.currentIndex() == -1:
            return

        path = self.imageComboBox.currentData()
        name = self.nameLineEdit.text()
        h = self.hParamSlider.value()
        tWS = self.tWSSpinBox.value()
        sWS = self.sWSSpinBox.value()

        self.startCalc.emit(path, name, h, tWS, sWS)

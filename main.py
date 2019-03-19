import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ImageFilter import ImageFilter

if __name__ == '__main__':
    app = QApplication(sys.argv)

    imageFilter = ImageFilter()

    sys.exit(app.exec_())

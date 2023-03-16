"""
Добавим размеры нашего приложения, название и отключим возможность изменять размер окна
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа расчета')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(500, 350)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

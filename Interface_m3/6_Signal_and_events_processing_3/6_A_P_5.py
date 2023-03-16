"""
Добавим два текстовых поля и укажем, чтобы наш слой с текстом был выровнен по верхнему краю
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа расчета')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(500, 350)

        self.base_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.base_layout)

        self.text_layout = QtWidgets.QHBoxLayout()

        self.base_layout.addLayout(self.text_layout)
        self.setLayout(self.base_layout)

        self.text1 = QtWidgets.QLineEdit()
        self.text_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.text2 = QtWidgets.QLineEdit()
        self.text_layout.addWidget(self.text1)
        self.text_layout.addWidget(self.text2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
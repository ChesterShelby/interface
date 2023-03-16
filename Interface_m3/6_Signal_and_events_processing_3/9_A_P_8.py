"""
Внешний вид программы можно и доработать, но пока нам для примера подойдет и данный вариант.
Теперь добавим методы, которые мы будем вызывать при нажатии на кнопки
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
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

        self.label = QtWidgets.QLabel(f'Ответ:')

        # Укажем выравнивание, шрифт и размер шрифта
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setFont(QtGui.QFont('Arial', 15))

        # Добавим нашу надпись в окно
        self.base_layout.addWidget(self.label)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.base_layout.addLayout(self.button_layout)

        # Теперь создадим две кнопки и добавим их в наш новый слой
        self.area_button = QtWidgets.QPushButton('Площадь')
        self.perimetr_button = QtWidgets.QPushButton('Периметр')

        self.button_layout.addWidget(self.area_button)
        self.button_layout.addWidget(self.perimetr_button)

    def get_area(self):
        print('Нажата кнопка расчета площади')

    def get_perimetr(self):
        print('Нажата кнопка расчета периметра')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

"""
self.setWindowIcon(QIcon('icon.png')) позволяет нам установить в качестве иконки приложения, указанное изображение.

self.setFixedSize(500, 350) - данной строчкой мы указываем, что у нашего окна будет фиксированный размер 500 на 350.

Теперь давайте добавим необходимые компоненты на наше окно. В первую очередь нам необходимо добавить два текстовых поля,
для ввода ширины и высоты прямоугольника. Все компоненты, которые мы будем добавлять нам потребуется отпозиционировать
в главном окне. Про позиционирование элементов подробно мы поговорим позже, а пока просто создадим базовый слой,
который мы добавим на наше окно
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

        self.base_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.base_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

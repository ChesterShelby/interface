"""
Для закрепления новой информации давайте напишем небольшую простенькую программу для расчета площади и периметра прямоугольника.
Для начала создадим небольшой каркас приложения
"""

import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()



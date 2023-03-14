"""
При перемещении и изменении размеров окна вызываются следующие методы:

moveEvent(self, <event>) — непрерывно вызывается при перемещении окна.
Через параметр <event> доступен экземпляр класса QMoveEvent.
Получить координаты окна позволяют следующие методы этого класса:

    • pos() — возвращает экземпляр класса QPoint с текущими координатами;
    • oldPos() — возвращает экземпляр класса QPoint с предыдущими координатами;

resizeEvent(self, <event>) — непрерывно вызывается при изменении размеров окна.
Через параметр <event> доступен экземпляр класса QResizeEvent.
Получить размеры окна позволяют следующие методы этого класса:

    • size() — возвращает экземпляр класса QSize с текущими размерами;
    • oldSize() — возвращает экземпляр класса QSize с предыдущими размерами.

"""

from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def moveEvent(self, e):
        print(f"x = {e.pos().x()}; y = {e.pos().y()}")
        QtWidgets.QWidget.moveEvent(self, e)  # Отправляем дальше

    def resizeEvent(self, e):
        print(f"w = {e.size().width()}; h = {e.size().height()}")
        QtWidgets.QWidget.resizeEvent(self, e)  # Отправляем дальше


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

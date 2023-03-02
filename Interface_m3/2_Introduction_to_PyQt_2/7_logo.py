import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets


def load_data(sp):
    for i in range(1, 11):  # Имитируем процесс
        time.sleep(2)  # Что-то загружаем
        sp.showMessage("Загрузка данных... {0}%".format(i * 10),
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
        QtWidgets.qApp.processEvents()  # Запускаем оборот цикла


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Закрыть окно")
        self.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("logo.jpg"))
    splash.show()  # Отображаем заставку
    QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
    window = MyWindow()
    window.setWindowTitle("Использование класса QSplashScreen")
    window.resize(300, 30)
    load_data(splash)  # Загружаем данные
    window.show()

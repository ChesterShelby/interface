"""
Создадим окно с четырьмя кнопками. Для кнопки "Нажми меня" назначим обработчик сигнала clicked.
Чтобы информировать о нажатии кнопки, выведем сообщение в окно консоли. Для кнопок Блокировать,
"Разблокировать" и "Удалить" обработчик создадим обработчики,
которые будут изменять статус обработчика для кнопки "Нажми меня".
"""

import sys
from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Блокировка и удаление обработчика")
        self.resize(300, 150)
        self.button1 = QtWidgets.QPushButton("Нажми меня")
        self.button2 = QtWidgets.QPushButton("Блокировать")
        self.button3 = QtWidgets.QPushButton("Разблокировать")
        self.button4 = QtWidgets.QPushButton("Удалить обработчик")
        self.button3.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.button3.clicked.connect(self.on_clicked_button3)
        self.button4.clicked.connect(self.on_clicked_button4)

    @QtCore.pyqtSlot()
    def on_clicked_button1(self):
        print("Нажата кнопка button1")

    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        self.button1.blockSignals(True)
        self.button2.setEnabled(False)
        self.button3.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_clicked_button3(self):
        self.button1.blockSignals(False)
        self.button2.setEnabled(True)
        self.button3.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_button4(self):
        self.button1.clicked.disconnect(self.on_clicked_button1)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

"""
Если нажать кнопку Нажми меня, в окно консоли будет выведена строка Нажата кнопка button1. Нажатие кнопки 
Блокировать производит блокировку обработчика — теперь при нажатии кнопки Нажми меня никаких сообщений 
в окно консоли не выводится. Отменить блокировку можно с помощью кнопки Разблокировать. 
Нажатие кнопки Удалить обработчик производит полное удаление обработчика — в этом случае,
чтобы обрабатывать нажатие кнопки Нажми меня, необходимо заново назначить обработчик.
"""

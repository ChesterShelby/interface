"""
Переделаем предыдущую программу, инсценировав с помощью цикла длительную операцию, которая выполняется 20 секунд
"""

import sys
import time

from PyQt5 import QtWidgets


def on_clicked():
    button.setDisabled(True)  # Делаем кнопку неактивной
    for i in range(1, 21):
        QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
        time.sleep(1)  # "Засыпаем" на 1 секунду
        print("step -", i)
    button.setDisabled(False)  # Делаем кнопку активной


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Запустить процесс")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())


# """
# В этом примере длительная операция разбита на одинаковые этапы, после выполнения каждого из которых выполняется выход
# в основной цикл приложения. Теперь при перекрытии окна и повторном его отображении оно будет перерисовано —
# таким образом, приложение по-прежнему будет взаимодействовать с системой, хотя и с некоторой задержкой.
# """

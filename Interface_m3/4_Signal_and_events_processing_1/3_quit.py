"""
Классы PyQt 5 поддерживают ряд методов, специально предназначенных для использования в качестве обработчиков сигналов.
Такие методы называются слотами. Например, класс QApplication поддерживает слот quit(), завершающий текущее приложение.
"""

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Завершить работу")
button.clicked.connect(app.quit)
button.show()
sys.exit(app.exec_())

"""
Давайте начнем рассматривать основные компоненты.
Класс QToolBox позволяет создать «аккордеон» — компонент с несколькими вкладками,
в котором изначально отображается содержимое только одной вкладки, а у остальных видимы лишь заголовки.
После щелчка мышью на заголовке вкладки она открывается, а остальные сворачиваются. Иерархия наследования выглядит так:

(QObject, QPaintDevice) — QWidget — QFrame — QToolBox

Конструктор класса QToolBox имеет следующий формат:
<Объект> = QToolBox([parent=<Родитель>][, flags=<Тип окна>])

В параметре parent указывается ссылка на родительский компонент. Если он не указан или имеет значение None,
компонент будет обладать своим собственным окном. В параметре flags может быть указан тип окна.
"""

from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QToolBox")
window.resize(200, 100)
toolBox = QtWidgets.QToolBox()
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 3"), "Вкладка &3")
toolBox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())

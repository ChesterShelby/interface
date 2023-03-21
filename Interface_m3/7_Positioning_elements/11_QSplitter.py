"""
Класс QSplitter позволяет изменять размеры добавленных компонентов, взявшись мышью за границу между компонентами.
Иерархия наследования выглядит так:
(QObject, QPaintDevice) — QWidget — QFrame — QSplitter

Конструктор класса QSplitter имеет два формата:
<Объект> = QSplitter([parent=<Родитель>])
<Объект> = QSplitter(<Ориентация>[, parent=<Родитель>])

В параметре parent указывается ссылка на родительский компонент.
Если таковой не указан или имеет значение None, компонент будет обладать своим собственным окном.
Параметр <Ориентация> задает ориентацию размещения компонентов.
Могут быть заданы атрибуты Horizontal (по горизонтали) или Vertical (по вертикали) класса QtCore.Qt.
Если параметр не указан, компоненты размещаются по горизонтали.
"""

from PyQt5 import QtCore, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSplitter")
window.resize(200, 200)
splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
label1 = QtWidgets.QLabel("Содержимое компонента 1")
label2 = QtWidgets.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())

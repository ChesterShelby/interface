"""
Любой пользовательский метод можно сделать слотом, для чего необходимо перед его определением вставить декоратор
@pyqtSlot(). Формат декоратора:
@QtCore.pyqtSlot(*<Типы данных>, name=None, result=None)

В параметре <Типы данных> через запятую указываются типы данных параметров, принимаемых слотом, например: bool или int.
Если метод не принимает параметров, параметр <Типы данных> не указывается.
В именованном параметре name можно передать название слота в виде строки —
это название станет использоваться вместо названия метода, а если параметр name не задан,
название слота будет совпадать с названием метода. Именованный параметр result предназначен для указания типа данных,
возвращаемых методом, если параметр не задан, то метод ничего не возвращает. Чтобы создать перегруженную версию слота,
декоратор указывается последовательно несколько раз с разными типами данных.
"""

from PyQt5 import QtCore, QtWidgets
import sys


class MyClass(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        print("Кнопка нажата. Слот on_clicked()")

    @QtCore.pyqtSlot(bool, name="myslot")
    def on_clicked2(self, status):
        print("Кнопка нажата. Слот myslot(bool)", status)


obj = MyClass()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Нажми меня")
button.clicked.connect(obj.on_clicked)
button.clicked.connect(obj.myslot)
button.show()
sys.exit(app.exec_())

"""
Загрузить UI-файл позволяет также функция loadUiType() — она возвращает кортеж из двух элементов:
ссылки на класс формы и ссылки на базовый класс. Так как функция возвращает ссылку на класс, а не на экземпляр класса,
мы можем создать множество экземпляров класса. После создания экземпляра класса формы необходимо вызвать метод setupUi()
и передать ему указатель self
"""

import sys
from PyQt5 import QtWidgets, uic


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("MyForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

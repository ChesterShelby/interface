"""
Загрузить UI-файл можно и вне класса, после чего указать класс формы во втором параметре в списке наследования,
в этом случае наш класс наследует все методы класса формы
"""

import sys
from PyQt5 import QtWidgets, uic

Form, Base = uic.loadUiType("MyForm.ui")


class MyWindow(QtWidgets.QWidget, Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

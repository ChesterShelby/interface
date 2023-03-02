"""
Если во втором параметре указать ссылку на экземпляр класса, то все компоненты формы
будут доступны через указатель self
"""

import sys
from PyQt5 import QtWidgets, uic


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("MyForm.ui", self)  # вот тута
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

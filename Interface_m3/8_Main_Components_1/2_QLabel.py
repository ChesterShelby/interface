import sys
from PyQt5 import QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelA = QtWidgets.QLabel(windowExample)
    labelA.setText('Label Пример')
    windowExample.setWindowTitle('Label Example')
    windowExample.setGeometry(100, 100, 300, 200)
    labelA.move(100, 40)
    windowExample.show()
    sys.exit(app.exec_())


main()

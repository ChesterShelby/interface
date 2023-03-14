"""
При закрытии окна нажатием кнопки Закрыть в его заголовке или вызовом метода close() в коде выполняется метод
closeEvent(self, <event>). Через параметр <event> доступен экземпляр класса QCloseEvent.
Чтобы предотвратить закрытие окна, у объекта события следует вызвать метод ignore(), в противном случае — метод accept().

В качестве примера по нажатию кнопки Закрыть выведем стандартное диалоговое окно с запросом подтверждения закрытия окна.
Если пользователь нажмет кнопку Да, закроем окно, а если щелкнет кнопку Нет или просто закроет диалоговое окно,
не будем его закрывать.

"""

from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение закрытия окна",
                                                "Вы действительно хотите закрыть окно?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

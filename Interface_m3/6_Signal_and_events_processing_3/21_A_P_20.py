"""
Ну и напоследок давайте добавим, чтобы при закрытии окна нас спрашивали уверены ли мы, что хотим закрыть окно
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа расчета')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(500, 350)

        self.base_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.base_layout)

        self.text_layout = QtWidgets.QHBoxLayout()

        self.base_layout.addLayout(self.text_layout)
        self.setLayout(self.base_layout)

        self.text1 = QtWidgets.QLineEdit()
        self.text_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.text2 = QtWidgets.QLineEdit()
        self.text_layout.addWidget(self.text1)
        self.text_layout.addWidget(self.text2)

        self.label = QtWidgets.QLabel(f'Ответ:')

        # Укажем выравнивание, шрифт и размер шрифта
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setFont(QtGui.QFont('Arial', 15))

        # Добавим нашу надпись в окно
        self.base_layout.addWidget(self.label)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.base_layout.addLayout(self.button_layout)

        # Теперь создадим две кнопки и добавим их в наш новый слой
        self.area_button = QtWidgets.QPushButton('Площадь')
        self.perimetr_button = QtWidgets.QPushButton('Периметр')

        self.button_layout.addWidget(self.area_button)
        self.button_layout.addWidget(self.perimetr_button)

        self.area_button.clicked.connect(self.get_area)
        self.perimetr_button.clicked.connect(self.get_perimetr)

    def get_area(self):
        try:
            text1 = float(self.text1.text())
            text2 = float(self.text2.text())
            result = text1 * text2
            self.label.setText(f'Ответ: {result}')
        except ValueError:
            self.label.setText('Вы ошиблись при вводе')
        finally:
            timer = QtCore.QTimer()
            timer.setInterval(1000)
            timer.singleShot(5000, self.reset_data)

    def get_perimetr(self):
        try:
            text1 = float(self.text1.text())
            text2 = float(self.text2.text())
            result = (text1 + text2) * 2
            self.label.setText(f'Ответ: {result}')
        except ValueError:
            self.label.setText('Вы ошиблись при вводе')
        finally:
            timer = QtCore.QTimer()
            timer.setInterval(1000)
            timer.singleShot(5000, self.reset_data)

    def reset_data(self):
        self.label.setText(f'Ответ: ')
        self.text1.clear()
        self.text2.clear()
        self.text1.setFocus()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            'Информация',
            'Вы уверены, что хотите выйти?',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            window.close()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

"""
Как мы видим программа полностью готова. Да внешний вид она имеет довольно простой, 
но пока мы не сталкивались с темами позиционирования и применения стилей для нашей программы. 
Это мы научимся делать позже.
"""

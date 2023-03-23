"""
Для ввода даты и времени предназначены классы QDateTimeEdit (ввод даты и времени),
QDateEdit (ввод даты) и QTimeEdit (ввод времени). Поля могут содержать кнопки,
которые позволяют щелчками мыши увеличивать и уменьшать значение внутри поля.

Иерархия наследования:
(QObject, QPaintDevice) — QWidget — QAbstractSpinBox — QDateTimeEdit
(QObject, QPaintDevice) — QWidget — QAbstractSpinBox — QDateTimeEdit — QDateEdit
(QObject, QPaintDevice) — QWidget — QAbstractSpinBox — QDateTimeEdit — QTimeEdit

Форматы конструкторов классов:
<Объект> = QDateTimeEdit([parent=<Родитель>])
<Объект> = QDateTimeEdit(<QDateTime>[, parent=<Родитель>])
<Объект> = QDateTimeEdit(<QDate>[, parent=<Родитель>])

<Объект> = QDateTimeEdit(<QTime>[, parent=<Родитель>])
<Объект> = QDateEdit([parent=<Родитель>])
<Объект> = QDateEdit(<QDate>[, parent=<Родитель>])
<Объект> = QTimeEdit([parent=<Родитель>])
<Объект> = QTimeEdit(<QTime>[, parent=<Родитель>])

В параметре <QDateTime> можно указать экземпляр класса QDateTime или экземпляр класса datetime из языка Python.
Преобразовать экземпляр класса QDateTime в экземпляр класса datetime позволяет метод toPyDateTime() класса QDateTime:
"""

from PyQt5.QtWidgets import (QWidget, QDateTimeEdit, QHBoxLayout,
                             QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        sbox = QDateTimeEdit(self)

        hbox.addWidget(sbox)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('DateTimeEdit')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

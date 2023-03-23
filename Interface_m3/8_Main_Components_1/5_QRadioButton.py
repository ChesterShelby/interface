"""
Переключатели (иногда их называют радиокнопками) всегда используются группами.
В такой группе может быть установлен только один переключатель — при попытке установить другой переключатель
ранее установленный сбрасывается. Для объединения переключателей в группу можно воспользоваться классом QGroupBox, а также классом QButtonGroup.

Переключатель реализуется классом QRadioButton. Иерархия наследования:
(QObject, QPaintDevice) — QWidget — QAbstractButton — QRadioButton

Конструктор класса QRadioButton имеет два формата:
<Объект> = QRadioButton([parent=<Родитель>])
<Объект> = QRadioButton(<Текст>[, parent=<Родитель>])

Класс QRadioButton наследует все методы класса QAbstractButton. Установить или сбросить переключатель позволяет метод setChecked(),
а проверить его текущее состояние можно с помощью метода isChecked().
Отследить изменение состояния можно в обработчике сигнала toggled(<Состояние>),
в параметре которого передается логическая величина, указывающая новое состояние переключателя.
"""

from PyQt5.QtWidgets import (QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        rb1 = QRadioButton("Large", self)
        rb1.toggled.connect(self.updateLabel)

        rb2 = QRadioButton("Middle", self)
        rb2.toggled.connect(self.updateLabel)

        rb3 = QRadioButton("Small", self)
        rb3.toggled.connect(self.updateLabel)

        self.label = QLabel('', self)

        hbox.addWidget(rb1)
        hbox.addWidget(rb2)
        hbox.addWidget(rb3)

        vbox.addSpacing(15)

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(400, 300, 350, 250)
        self.setWindowTitle('QRadioButton')
        self.show()

    def updateLabel(self, _):
        rbtn = self.sender()

        if rbtn.isChecked():
            self.label.setText(rbtn.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

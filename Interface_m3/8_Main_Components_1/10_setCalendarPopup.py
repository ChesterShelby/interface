"""
В качестве параметра <QDate> можно указать экземпляр класса QDate или экземпляр класса date из языка Python.
Преобразовать экземпляр класса QDate в экземпляр класса date позволяет метод toPyDate() класса QDate.

В параметре <QTime> можно указать экземпляр класса QTime или экземпляр класса time из языка Python.
Преобразовать экземпляр класса QTime в экземпляр класса time позволяет метод toPyTime() класса QTime.

Классы QDateTime, QDate и QTime определены в модуле QtCore.

Класс QDateTimeEdit наследует все методы из класса QAbstractSpinBox и дополнительно реализует следующие методы:

setDateTime(<QDateTime>) — устанавливает дату и время. В качестве параметра указывается экземпляр класса QDateTime
или экземпляр класса datetime из языка Python. Метод является слотом;

setDate(<QDate>) — устанавливает дату. В качестве параметра указывается экземпляр
класса QDate или экземпляр класса date языка Python. Метод является слотом;

setTime(<QTime>) — устанавливает время. В качестве параметра указывается экземпляр
класса QTime или экземпляр класса time из языка Python. Метод является слотом;

dateTime() — возвращает экземпляр класса QDateTime с датой и временем;

date() — возвращает экземпляр класса QDate с датой;

time() — возвращает экземпляр класса QTime со временем;

setDateTimeRange(<Минимум>, <Максимум>), setMinimumDateTime(<Минимум>) и setMaximumDateTime(<Максимум>) —
задают минимальное и максимальное допустимые значения для даты и времени.
В параметрах указывается экземпляр класса QDateTime или экземпляр класса datetime из языка Python;

setDateRange(<Минимум>, <Максимум>), setMinimumDate(<Минимум>) и setMaximumDate(<Максимум>) —
задают минимальное и максимальное допустимые значения для даты.
В параметрах указывается экземпляр класса QDate или экземпляр класса date из языка Python;

setTimeRange(<Минимум>, <Максимум>), setMinimumTime(<Минимум>) и setMaximumTime(<Максимум>) —
задают минимальное и максимальное допустимые значения для времени.
В параметрах указывается экземпляр класса QTime или экземпляр класса time из языка Python;

setDisplayFormat(<Формат>) — задает формат отображения даты и времени. В качестве параметра указывается строка,
содержащая специальные символы. Пример задания строки формата:
dateTimeEdit.setDisplayFormat("dd.MM.yyyy HH:mm:ss")

setTimeSpec(<Зона>) — задает зону времени. В качестве параметра можно указать атрибуты LocalTime, UTC или OffsetFromUTC класса QtCore.Qt;

setCalendarPopup(<Флаг>) — если в качестве параметра указано значение True, то дату можно будет выбрать с помощью календаря,
который появится на экране при щелчке на кнопке с направленной вниз стрелкой, выведенной вместо стандартных кнопок-стрелок
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
        sbox.setCalendarPopup(True)
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

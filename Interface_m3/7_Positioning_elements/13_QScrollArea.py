"""
Класс QScrollArea реализует область с полосами прокрутки. Если компонент не помещается в размеры области,
полосы прокрутки будут отображены автоматически. Иерархия наследования выглядит так:

(QObject, QPaintDevice) — QWidget — QFrame —QAbstractScrollArea — QScrollArea
Конструктор класса QScrollArea имеет следующий формат:
<Объект> = QScrollArea([<Родитель>])

Класс QScrollArea поддерживает следующие методы:

setWidget(<Компонент>) — помещает компонент в область прокрутки;

setWidgetResizable(<Флаг>) — если в качестве параметра указано значение True,
при изменении размеров области будут изменяться и размеры компонента. Значение False запрещает изменение размеров компонента;

setAlignment(<Выравнивание>) — задает местоположение компонента внутри области,
когда размеры области больше размеров компонента:
scrollArea.setAlignment(QtCore.Qt.AlignCenter)

ensureVisible(<X>, <Y>[, xMargin=50][, yMargin=50]) — прокручивает область к точке с координатами (<X>, <Y>) и полями xMargin и yMargin;

ensureWidgetVisible(<Компонент>[, xMargin=50][, yMargin=50]) — прокручивает область таким образом, чтобы <Компонент> был видим;

widget() — возвращает ссылку на компонент, который расположен внутри области, или значение None;

takeWidget() — удаляет компонент из области и возвращает ссылку на него. Сам компонент не удаляется.


Класс QScrollArea наследует следующие методы из класса QAbstractScrollArea:

horizontalScrollBar() — возвращает ссылку на горизонтальную полосу прокрутки (экземпляр класса QScrollBar);

verticalScrollBar() — возвращает ссылку на вертикальную полосу прокрутки (экземпляр класса QScrollBar);

setHorizontalScrollBarPolicy(<Режим>) — устанавливает режим отображения горизонтальной полосы прокрутки;

setVerticalScrollBarPolicy(<Режим>) — устанавливает режим отображения вертикальной полосы прокрутки.

В параметре <Режим> могут быть указаны следующие атрибуты из класса QtCore.Qt:
• ScrollBarAsNeeded — 0 — полоса прокрутки отображается только в том случае, если размеры компонента больше размеров области;
• ScrollBarAlwaysOff — 1 — полоса прокрутки никогда не отображается;
• ScrollBarAlwaysOn — 2 — полоса прокрутки отображается всегда.
"""

from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 500, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        scroll = QScrollBar(self)
        scroll.setGeometry(100, 50, 30, 200)
        label = QLabel("Python", self)
        label.setGeometry(200, 100, 300, 80)
        scroll.valueChanged.connect(lambda: do_action())

        def do_action():
            value = scroll.value()
            label.setText("Current Value : " + str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

"""
Командная кнопка используется для запуска какой-либо операции. Кнопка реализуется
с помощью класса QPushButton. Иерархия наследования:
(QObject, QPaintDevice) — QWidget — QAbstractButton — QPushButton

Конструктор класса QPushButton имеет три формата:
<Объект> = QPushButton([parent=<Родитель>])
<Объект> = QPushButton(<Текст>[, parent=<Родитель>])
<Объект> = QPushButton(<QIcon>, <Текст>[, parent=<Родитель>])

В параметре parent указывается ссылка на родительский компонент. Если таковой не задан
или имеет значение None, компонент будет обладать своим собственным окном. Параметр
<Текст> позволяет задать текст, который отобразится на кнопке, а параметр <QIcon> — добавить перед текстом значок.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


# Define class to create a single push button
class ButtonExample(QWidget):

    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Нажми меня', self)
        self.btn.setToolTip('Кнопка')
        self.btn.setGeometry(100, 20, 100, 30)
        self.btn.clicked.connect(self.on_clicked)
        self.msgLabel = QLabel('', self)
        self.msgLabel.setGeometry(90, 60, 290, 60)

        self.setWindowTitle('Использование кнопки')
        self.setGeometry(10, 10, 300, 150)

        self.move(850, 300)
        self.show()

    def on_clicked(self):
        self.msgLabel.setText('Кнопка нажата.')


app = QApplication(sys.argv)
button = ButtonExample()
app.exec()

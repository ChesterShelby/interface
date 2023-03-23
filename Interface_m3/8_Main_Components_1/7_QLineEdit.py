"""
Однострочное текстовое поле предназначено для ввода и редактирования текста небольшого объема.
С его помощью можно также отобразить вводимые символы в виде звездочек (чтобы скрыть пароль)
или вообще не отображать их (что позволит скрыть длину пароля).
Поле поддерживает технологию drag & drop, стандартные комбинации клавиш быстрого доступа,
работу с буфером обмена и многое другое.
Однострочное текстовое поле реализуется классом QLineEdit. Иерархия наследования:
(QObject, QPaintDevice) — QWidget — QLineEdit

Конструктор класса QLineEdit имеет два формата:
<Объект> = QLineEdit([parent=<Родитель>])
<Объект> = QLineEdit(<Текст>[, parent=<Родитель>])

В параметре parent указывается ссылка на родительский компонент.
Если родитель не указан или имеет значение None, компонент будет обладать своим собственным окном.
Параметр <Текст> позволяет задать текст, который будет отображен в текстовом поле.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

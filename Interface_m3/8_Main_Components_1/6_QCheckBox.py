"""
Флажок предназначен для включения или выключения какой-либо опции и может находиться в нескольких состояниях:
установленном, сброшенном и промежуточном (неопределенном) — последнее состояние может быть запрещено программно.
Флажок реализуется с помощью класса QCheckBox. Иерархия наследования:
(QObject, QPaintDevice) — QWidget — QAbstractButton — QCheckBox

Конструктор класса QCheckBox имеет два формата:
<Объект> = QCheckBox([parent=<Родитель>])
<Объект> = QCheckBox(<Текст>[, parent=<Родитель>])

Класс QCheckBox наследует все методы класса QAbstractButton, а также добавляет несколько новых:

setCheckState(<Статус>) — задает состояние флажка. Могут быть указаны следующие атрибуты класса QtCore.Qt:

• Unchecked — 0 — флажок сброшен;
• PartiallyChecked — 1 — флажок находится в промежуточном состоянии;
• Checked — 2 — флажок установлен;

checkState() — возвращает текущее состояние флажка;

setTristate([<Флаг>=True]) — если в качестве параметра указано значение True (значение по умолчанию),
флажок может находиться во всех трех состояниях. По умолчанию поддерживаются только установленное и сброшенное состояния;

isTristate() — возвращает значение True, если флажок поддерживает три состояния, и False — если только два.

Чтобы перехватить изменение состояния флажка, следует назначить обработчик сигнала stateChanged(<Состояние>).
Через параметр внутри обработчика доступно новое состояние флажка, заданное в виде целого числа.
Если используется флажок, поддерживающий только два состояния, установить или сбросить его позволяет метод setChecked(),
а проверить текущее состояние — метод isChecked().
Обработать изменение состояния можно в обработчике сигнала toggled(<Состояние>), параметр которого имеет логический тип.
"""

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

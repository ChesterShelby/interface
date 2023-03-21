"""
Помимо выравнивания компонентов по горизонтали и вертикали, существует возможность размещения компонентов внутри
ячеек сетки. Для этого предназначен класс QGridLayout. Иерархия его наследования:

(QObject, QLayoutItem) — QLayout — QGridLayout

Создать экземпляр класса QGridLayout можно следующим образом:
<Объект> = QGridLayout([<Родитель>])

В необязательном параметре можно указать ссылку на родительский компонент.
Если таковой не указан, следует передать ссылку на сетку в метод setLayout() родительского компонента.
Код, иллюстрирующий типичный пример использования класса QGridLayout, представлен ниже.
"""

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()  # Родительский компонент — окно
window.setWindowTitle("QGridLayout")
window.resize(150, 100)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
grid = QtWidgets.QGridLayout()  # Создаем сетку
grid.addWidget(button1, 0, 0)  # Добавляем компоненты
grid.addWidget(button2, 0, 1)
grid.addWidget(button3, 1, 0)
grid.addWidget(button4, 1, 1)
window.setLayout(grid)  # Передаем ссылку родителю
window.show()
sys.exit(app.exec_())

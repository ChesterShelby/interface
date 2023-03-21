"""
Класс QFormLayout позволяет выравнивать компоненты формы. Контейнер по умолчанию состоит из двух столбцов:
первый предназначен для вывода надписи, а второй — для вывода самого компонента.
При этом надпись связывается с компонентом, что позволяет назначать клавиши быстрого доступа,
указав символ & перед буквой внутри текста надписи.
По нажатию комбинации клавиш быстрого доступа (комбинация <Alt>+<буква>) в фокусе окажется компонент,
расположенный справа от надписи. Иерархия наследования выглядит так:

(QObject, QLayoutItem) — QLayout — QFormLayout

Создать экземпляр класса QFormLayout можно следующим образом:
<Объект> = QFormLayout([<Родитель>])

В необязательном параметре можно указать ссылку на родительский компонент.
Если таковой не указан, необходимо передать ссылку на контейнер в метод setLayout() родительского компонента.
"""

from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QFormLayout")
window.resize(300, 150)
lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("О&тправить")
button2 = QtWidgets.QPushButton("О&чистить")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtWidgets.QFormLayout()
form.addRow("&Название:", lineEdit)
form.addRow("&Описание:", textEdit)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())

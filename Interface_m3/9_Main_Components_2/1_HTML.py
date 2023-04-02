"""
Многострочное текстовое поле предназначено для ввода и редактирования как простого
текста, так и текста в формате HTML. Поле поддерживает технологию drag & drop, стан-
дартные комбинации клавиш быстрого доступа, работу с буфером обмена и многое другое.
Многострочное текстовое поле реализуется с помощью класса QTextEdit. Иерархия насле-
дования:

(QObject, QPaintDevice) — QWidget — QFrame —QAbstractScrollArea — QTextEdit

Конструктор класса QTextEdit имеет два формата вызова:

<Объект> = QTextEdit([parent=<Родитель>])
<Объект> = QTextEdit(<Текст>[, parent=<Родитель>])

В параметре parent указывается ссылка на родительский компонент. Если параметр не указан или имеет значение None,
компонент будет обладать своим собственным окном. Параметр <Текст> позволяет задать текст в формате HTML,
который будет отображен в текстовом поле.
"""

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('Пример QTextEdit')

        # Определить начальный размер окна
        self.resize(300, 270)
        # Создать многострочное текстовое поле
        self.textEdit = QTextEdit()
        # Создать две кнопки
        self.btnPress1 = QPushButton("Показать текст")

        self.btnPress2 = QPushButton("Показать HTML")

        # Создание вертикального макета
        layout = QVBoxLayout()
        # Связанные элементы управления добавляются в вертикальный макет
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        # Установить макет
        self.setLayout(layout)

        # Привязать сигнал нажатия кнопки к соответствующей функции слота и нажать для запуска
        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        self.btnPress2.clicked.connect(self.btnPress2_clicked)

    def btnPress1_clicked(self):
        self.textEdit.setPlainText("Здравствуйте Нажмите кнопку")

    def btnPress2_clicked(self):
        self.textEdit.setHtml("<font color = 'red' size = '6'> <red> Здравствуйте, PyQt5! \nНажмите кнопку. </ font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())

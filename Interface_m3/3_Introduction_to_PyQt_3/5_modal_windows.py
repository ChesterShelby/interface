"""
Создадим два независимых окна. В первом окне разместим кнопку, по нажатию которой
откроется модальное окно, — оно будет блокировать только первое окно, но не второе. При
открытии модального окна отобразим его примерно по центру родительского окна.
"""


from PyQt5 import QtCore, QtWidgets
import sys


def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.Window)
    modalWindow.setWindowTitle("Модальное окно")
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center() - modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show()


app = QtWidgets.QApplication(sys.argv)
window1 = QtWidgets.QWidget()
window1.setWindowTitle("Обычное окно")
window1.resize(300, 100)
button = QtWidgets.QPushButton("Открыть модальное окно")
button.clicked.connect(show_modal_window)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window1.setLayout(vbox)
window1.show()
window2 = QtWidgets.QWidget()
window2.setWindowTitle("Это окно не будет блокировано при WindowModal")
window2.resize(500, 100)
window2.show()
sys.exit(app.exec_())

# Если запустить приложение и нажать кнопку Открыть модальное окно, откроется окно,
# выровненное примерно по центру родительского окна (произвести точное выравнивание вы сможете самостоятельно).
# При этом получить доступ к родительскому окну можно только после закрытия модального окна,
# второе же окно заблокировано не будет. Если заменить атрибут WindowModal атрибутом ApplicationModal,
# оба окна будут блокированы.

# Обратите внимание, что в конструктор модального окна мы передали ссылку на первое окно и атрибут Window.
# Если не указать ссылку, то окно заблокировано не будет, а если не указать атрибут, окно вообще не откроется.
# Кроме того, мы объявили переменную modalWindow глобальной, иначе при достижении конца функции переменная выйдет
# из области видимости, и окно будет автоматически удалено. Чтобы объект окна автоматически удалялся при закрытии окна,
# атрибуту WA_DeleteOnClose в методе setAttribute() было присвоено значение True.

# Модальные окна в большинстве случаев являются диалоговыми.
# Для работы с такими окнами в PyQt предназначен класс QDialog, который автоматически выравнивает окно по
# центру экрана или родительского окна. Кроме того, этот класс предоставляет множество специальных методов,
# позволяющих дождаться закрытия окна, определить статус завершения и выполнить другие действия.

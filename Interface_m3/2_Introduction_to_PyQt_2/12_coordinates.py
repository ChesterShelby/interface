"""
Чтобы получить координаты окна с учетом высоты заголовка и ширины границ, следует
воспользоваться методом frameGeometry(). И в этом случае полные размеры окна доступны
только после отображения окна. Метод возвращает экземпляр класса QRect:
"""

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()  # Создаем окно
window.setWindowTitle("Заголовок окна")  # Указываем заголовок
window.resize(300, 50)  # Минимальные размеры
window.show()  # Отображаем окно
rect = window.geometry()
print(rect.left(), rect.top())
print(rect.width(), rect.height())
rect = window.frameGeometry()
print(rect.left(), rect.top())
print(rect.width(), rect.height())
sys.exit(app.exec_())

"""
Сделать окно полупрозрачным позволяет метод setWindowOpacity() класса QWidget. Формат
метода:
setWindowOpacity(<Вещественное число от 0.0 до 1.0>)

Число 0.0 соответствует полностью прозрачному окну, а число 1.0 — отсутствию прозрачности.
Для получения степени прозрачности окна из программы предназначен метод windowOpacity().
Выведем окно со степенью прозрачности 0.5
"""

from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Полупрозрачное окно")
window.resize(300, 100)
window.setWindowOpacity(0.5)
window.show()
print(window.windowOpacity())
sys.exit(app.exec_())

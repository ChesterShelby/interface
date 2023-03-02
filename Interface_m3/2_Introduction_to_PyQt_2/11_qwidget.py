from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()  # Создаем окно
window.setWindowTitle("Заголовок окна")  # Указываем заголовок
window.resize(300, 50)  # Минимальные размеры
window.show()  # Отображаем окно
print(window.width(), window.height())
print(window.frameSize().width(),
      window.frameSize().height())
sys.exit(app.exec_())

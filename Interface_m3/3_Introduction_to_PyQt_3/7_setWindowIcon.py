from PyQt5 import QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка в заголовке окна")
window.resize(300, 100)
ico = QtGui.QIcon("logo.jpg")
window.setWindowIcon(ico)  # Значок для окна
app.setWindowIcon(ico)  # Значок приложения
window.show()
sys.exit(app.exec_())

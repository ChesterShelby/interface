from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна по центру экрана")
window.resize(300, 100)
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec_())

# В этом примере мы воспользовались методами width() и height(), которые не учитывают высоту заголовка и ширину границ.
# В большинстве случаев этого способа достаточно. Если же при выравнивании необходима точность,
# то для получения размеров окна можно воспользоваться методом frameSize().

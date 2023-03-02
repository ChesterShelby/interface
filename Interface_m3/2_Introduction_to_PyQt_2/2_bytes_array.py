"""
QByteArray — массив байтов. Преобразуется в тип bytes:
"""

from PyQt5 import QtCore
arr = QtCore.QByteArray(bytes("str", "cp1251"))
print(arr)

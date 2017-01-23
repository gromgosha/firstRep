# coding: utf-8

    #файл main только для запуска приложения

import sys
from PyQt5.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
from Core.DataBase import DataBase

if __name__ == '__main__':
    app = QApplication(sys.argv)

    db = DataBase()
    db.connect()

    m = MainWindow()
    m.show()

    sys.exit(app.exec_())





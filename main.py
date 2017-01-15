

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Browser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()

    def initUi(self):
        loadUi('main_window.ui', self)      #подключение файла и указание куда сохранять
        self.statusBar().showMessage('Приложение запущено')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    browser = Browser()
    browser.show()

    sys.exit(app.exec_())





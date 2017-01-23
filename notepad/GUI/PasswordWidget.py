from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi

class PasswordWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
       
    def init_ui(self):
        loadUi('GUI/UI/password_widget.ui', self)
   

    # def changedText(self):
    #     self.loginBtn.setEnabled(True)


    #.setEchoMode(EchoMode)
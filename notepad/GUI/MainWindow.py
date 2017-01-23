

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.uic import loadUi

from .notesWidget import NotesWidget
# from .UI.UI_password_widget import Ui_Form
from .PasswordWidget import PasswordWidget
from .ErrorWidget import ErrorWidget

from Core.NoteModel import NoteModel


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        loadUi('GUI/UI/main_window.ui', self)       #подключение файла
        
        self.notesWidget = NotesWidget(NoteModel(self), self)
        self.passwordWidget = PasswordWidget(self)
        self.errorWidget = ErrorWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)
        self.stackedWidget.addWidget(self.passwordWidget)
        self.stackedWidget.addWidget(self.errorWidget)
        self.stackedWidget.setCurrentWidget(self.passwordWidget)       #указываем какой виджет отобразить в stackedWidget
        self.toolBar.setEnabled(False)
        self.menuChange.setEnabled(False)

    def init_signals(self):
        self.passwordWidget.loginBtn.clicked.connect(self.loginClick)
        self.passwordWidget.showPasswordButton.clicked.connect(self.onPasswordShow)
                
    def retryClick(self):   #кнопка окна ERROR повторить
        self.stackedWidget.setCurrentWidget(self.passwordWidget)

    def exitClick(self):    #кнопка окна ERROR выйти
        self.close()
           
    def loginClick(self):     #кнопка "войти", при нажатии проверяет правильность логина и пароля
        if self.passwordWidget.loginEdit.text() == 'grom' and self.passwordWidget.passwordEdit.text() == '1234': 
            self.stackedWidget.setCurrentWidget(self.notesWidget)
            self.toolBar.setEnabled(True)
            self.menuChange.setEnabled(True)
        else:       #если логин(пароль) не правильный, открывается окно ERROR
            self.stackedWidget.setCurrentWidget(self.errorWidget)
            self.errorWidget.retryBtn.clicked.connect(self.retryClick)
            self.errorWidget.exitBtn.clicked.connect(self.exitClick)
        
    def onPasswordShow(self):       #показать/скрыть пароль
        if self.passwordWidget.showPasswordButton.isChecked():
            self.passwordWidget.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordWidget.passwordEdit.setEchoMode(QLineEdit.Password)

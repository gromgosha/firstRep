

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from Core.NoteModel import NoteModel

class NotesWidget(QWidget):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_model(model)
        self.init_ui()

    def init_ui(self):
        loadUi('GUI/UI/notes_widget.ui', self)

        self.notesView.setModel(self.__model)
        self.notesView.resizeColumnsToContents()

    def init_model(self, model):
        if isinstance(model, NoteModel):
            self.__model = model
            self.__model.select()       #добавление данных в модель
        else:
            raise RuntimeError('Переданная модель не NoteModel')

        


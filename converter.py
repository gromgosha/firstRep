
import sys
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout, QHBoxLayout 
    )

class CourseD(QObject):
    def get(self):
        return 58.7

class CourseE(QObject):
    def get(self):
        return 62.32

class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel ('Сумма в валюте', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertEuroBtn = QPushButton('Перевод Евро - Рубль', self)
        self.convertDollarBtn = QPushButton('Перевод Доллар - Рубль', self)
        self.clearBtn = QPushButton('Очистить', self)

        self.convertEuroBtn.setEnabled(False)            #отключение кнопки
        self.convertDollarBtn.setEnabled(False)
           
    def initSignals(self):
        self.convertEuroBtn.clicked.connect(self.euroClick)
        self.convertDollarBtn.clicked.connect(self.dollarClick)
        self.clearBtn.clicked.connect(self.clearClick)
        self.srcAmount.valueChanged.connect(self.onChangedValue)
        self.resultAmount.valueChanged.connect(self.onChangedValue)

    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)      # вертикальное расположение эл-тов
        #self.mainLayout = QHBoxLayout(self.w)       # горизонтальное расположение эл-тов
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertEuroBtn)
        self.mainLayout.addWidget(self.convertDollarBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(self.w)

    def euroClick(self):                        #перевод в евро
        value = self.srcAmount.value()
        res = self.resultAmount.value()
          
        if value:
            self.resultAmount.setValue(value / CourseE().get())
        if res:
            self.srcAmount.setValue(res * CourseE().get())
        
    def dollarClick(self):                      #перевод в доллары
        value = self.srcAmount.value()
        res = self.resultAmount.value()
          
        if value:
            self.resultAmount.setValue(value / CourseD().get())
        if res:
            self.srcAmount.setValue(res * CourseD().get())

    def clearClick(self):                       #очистиь поля
        self.srcAmount.setValue(0)
        self.resultAmount.setValue(0)
        self.convertEuroBtn.setEnabled(False)
        self.convertDollarBtn.setEnabled(False)

    def onChangedValue(self):          #включение кнопок перевода при изменении значений в полях ввода
        self.convertEuroBtn.setEnabled(True)
        self.convertDollarBtn.setEnabled(True)


    def keyPressEvent(self, e):         #при нажатии кнопки Enter очищаются поля ввода
        if e.key() == Qt.Key_Return:
            self.clearClick()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())
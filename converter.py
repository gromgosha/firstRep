
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout, QHBoxLayout 
    )

class CourseD(QObject):
    def get(self):
        return 61.0

class CourseE(QObject):
    def get(self):
        return 72.50


class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel ('Результат', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)            #блокировка изменения

        #self.convertBtn = QPushButton('Перевести', self)
        self.convertEuroBtn = QPushButton('Перевод Евро - Рубль', self)
        self.convertDollarBtn = QPushButton('Перевод Доллар - Рубль', self)
        self.clearBtn = QPushButton('Очистить', self)

        if self.srcAmount.value() == 0:
            self.convertEuroBtn.setEnabled(False)            #отключение кнопки

        elif self.srcAmount.value() > 0:
            self.convertEuroBtn.setEnabled(True)


        # val = self.srcAmount.value()
        # if val == 0.0:
        #     self.convertEuroBtn.setEnabled(False) 
        # else:
        #      self.convertEuroBtn.setEnabled(True)


        
    def initSignals(self):
        #self.convertBtn.clicked.connect(self.onClick)
        self.convertEuroBtn.clicked.connect(self.euroClick)
        self.convertDollarBtn.clicked.connect(self.dollarClick)
        self.clearBtn.clicked.connect(self.clearClick)

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
        #self.mainLayout.addWidget(self.convertBtn)

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
        self.srcAmount.setValue(0.0)
        self.resultAmount.setValue(0.0)



    # def onClick(self):
    #     value = self.srcAmount.value()
          
    #     if value:
    #         self.resultAmount.setValue(value / CourseD().get())


        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())



""" ДЗ   
1. Добавить кнопку "очистить"       +
2. Блокировать кнопку "перевести", если не задано значение   valueChanged, validate(с использованием xor - "^")
3. Добавить работу в обе стороны    +

ГУГЛИТЬ ДОКУМЕНТАЦИЮ

библиотека lxml

домашка на GitHub!!!

!!!keyPressEvent!!!, editingFinished - для обработки нажатия клавиш
"""
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget


#temp lista algorytmow itd do załadowania żeby ładowało cokolwiek
lista_algorytmy=['MD5']
lista_metody=['Brute force','Słownikowa']
lista_slowniki=['Zwierzeta','Imiona']

class App(QDialog):
    def __init__(self):
        super(App, self).__init__()
        loadUi("./UI/app.ui", self)

        self.combo_algorytmy.addItems(lista_algorytmy)
        self.combo_metody.addItems(lista_metody)
        self.combo_slowniki.addItems(lista_slowniki)

        self.combo_algorytmy.setCurrentIndex(-1)
        self.combo_metody.setCurrentIndex(-1)
        self.combo_slowniki.setCurrentIndex(-1)

        self.combo_metody.currentIndexChanged.connect(self.onMetodaChangedEvaluate)

    def onMetodaChangedEvaluate(self):
        temp=self.combo_metody.currentText()
        if(temp!='Słownikowa'):
            self.combo_slowniki.setCurrentIndex(-1)
            self.combo_slowniki.setDisabled(True)
        else:
            self.combo_slowniki.setDisabled(False)

    def onDecodeButtonClicked(self):
        self.lbl_wynik_out.setText('Decrypted text')

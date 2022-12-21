import sys

import pyrebase
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

from globalConfigs import *
from dbConn import *



class App(QDialog):
    def __init__(self):
        super(App, self).__init__()
        loadUi(appPath, self)
        self.dbConn = dbConn()

        #dbConn.PushSlownikFromFile(self.dbConn,"testSlownik","C:\\Users\\agata\\Desktop\\slownik.txt")

        #dbConn.GetSlowaZeSlownik(self.dbConn, "nazwaSlownika")

        lista_slowniki_db=dbConn.GetWszystkieSlowniki(self.dbConn)
        lista_algorytmy_db = dbConn.GetWszystkieAlgorytmy(self.dbConn)
        lista_metody_db = dbConn.GetWszystkieMetody(self.dbConn)


        self.combo_algorytmy.addItems(lista_algorytmy_db)
        self.combo_metody.addItems(lista_metody_db)
        self.combo_slowniki.addItems(lista_slowniki_db)

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
        nazwaMetody = self.combo_metody.currentText()
        nazwaAlgorytmu = self.combo_algorytmy.currentText()

        if nazwaMetody == 'Słownikowa':
            nazwaSlownika = self.combo_slowniki.currentText()

            listaSlow = []
            listaSlow = dbConn.GetSlowaZeSlownik(self.dbConn, nazwaSlownika)

            if nazwaAlgorytmu == "MD5":
                print("dictionary md5 implementation")

            else:
                print("Some other algorithm dictionary implementation")

        elif nazwaMetody == "Brute force":
            if nazwaAlgorytmu == "MD5":
                print("brute force md5 implementation")

            else:
                print("Some other algorithm brute force implementation")


        self.lbl_wynik_out.setText('to zlamane haslo')

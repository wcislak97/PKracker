import sys
import pyrebase
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import firebase_admin
from firebase_admin import credentials
import pyrebase

#app specific imports
from globalConfigs import *
from dbConn import *



class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi(adminPath, self)
        self.dbConn = dbConn()

        lista_slowniki_db = dbConn.GetWszystkieSlowniki(self.dbConn)
        self.combo_slowniki.addItems(lista_slowniki_db)
        self.combo_slowniki.setCurrentIndex(-1)

        self.combo_deleteDict.addItems(lista_slowniki_db)
        self.combo_deleteDict.setCurrentIndex(-1)

        lista_admins = dbConn.GetWszystkieAdminy(self.dbConn)
        self.combo_admins.addItems(lista_admins)
        self.combo_admins.setCurrentIndex(-1)



    def onAddAdminButtonClicked(self,inputEmail):
        try:
            results=dbConn.PushAdminFromInput(self.dbConn, inputEmail)
            if results !='':
                self.lbl_output_1.setText('Item added successfully')
                self.combo_admins.clear()
                lista_admins = dbConn.GetWszystkieAdminy(self.dbConn)
                self.combo_admins.addItems(lista_admins)
                self.combo_admins.setCurrentIndex(-1)
            else:
                self.lbl_output_1.setText('Error adding item')
        except:
            self.lbl_output_1.setText('Something went wrong')

    def onAddItemToSlownikButtonClicked(self,nazwaSlownika,slowo):
        listaSlow=dbConn.GetSlowaZeSlownik(self.dbConn,nazwaSlownika)

        if slowo in listaSlow:
            self.lbl_output_2.setText('Word already exists in this dictionary')
        else:
            try:
                results=dbConn.PushSlownik(self.dbConn, nazwaSlownika,slowo)
                if results != '':
                    self.lbl_output_2.setText('Item added successfully')
                else:
                    self.lbl_output_2.setText('Error adding item')
            except:
                self.lbl_output_2.setText('Something went wrong')

    def onAddDictionaryButtonClicked(self,nazwaSlownika,inputPath):
        lista_slowniki_db=dbConn.GetWszystkieSlowniki(self.dbConn)

        if nazwaSlownika in lista_slowniki_db:
            self.lbl_output_3.setText('Dictionary name already exists')
        else:
            try:
                dbConn.PushSlownikFromFile(self.dbConn,nazwaSlownika,inputPath)
                self.lbl_output_3.setText('Dictionary added successfully')
                self.combo_slowniki.clear()
                self.combo_deleteDict.clear()
                lista_slowniki_db = dbConn.GetWszystkieSlowniki(self.dbConn)
                self.combo_slowniki.addItems(lista_slowniki_db)
                self.combo_slowniki.setCurrentIndex(-1)

                self.combo_deleteDict.addItems(lista_slowniki_db)
                self.combo_deleteDict.setCurrentIndex(-1)


            except:
                self.lbl_output_3.setText('Something went wrong')

    def onRemoveAdminButtonClicked(self,inputAdmin):
        try:

            dbConn.RemoveAdmin(self.dbConn,inputAdmin)
            self.lbl_output_4.setText('Admin removed successfully')
            self.combo_admins.clear()
            lista_admins = dbConn.GetWszystkieAdminy(self.dbConn)
            self.combo_admins.addItems(lista_admins)
            self.combo_admins.setCurrentIndex(-1)
        except:
            self.lbl_output_4.setText('Something went wrong')


    def removeDictionaryButtonClicked(self,inputDictionary):
        try:
            dbConn.DeleteSlownik(self.dbConn,inputDictionary)
            self.lbl_output_5.setText('Dictionary removed successfully')

            self.combo_slowniki.clear()
            self.combo_deleteDict.clear()
            lista_slowniki_db = dbConn.GetWszystkieSlowniki(self.dbConn)
            self.combo_slowniki.addItems(lista_slowniki_db)
            self.combo_slowniki.setCurrentIndex(-1)

            self.combo_deleteDict.addItems(lista_slowniki_db)
            self.combo_deleteDict.setCurrentIndex(-1)
        except:
            self.lbl_output_5.setText('Something went wrong')
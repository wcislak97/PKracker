import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import re

# #app specific imports
from login import *
from firstPage import *
from registration import *
from app import *
from Admin import *
from dbConn import *

class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):

#creating objects of all the screens so we can open them later
        super().__init__()
        self.firstPage = FirstPage()
        self.loginScreen = LoginScreen()
        self.registration = RegistrationScreen()
        self.app = App();
        self.admin = Admin();
        self.dbConn=dbConn();

#adding widget so we can open them overall
        self.addWidget(self.firstPage)
        self.addWidget(self.loginScreen)
        self.addWidget(self.registration)
        self.addWidget(self.app)
        self.addWidget(self.admin)

#setting size
        self.setFixedWidth(1200)
        self.setFixedHeight(800)

#handling buttons
        self.firstPage.btn_login.clicked.connect(self.goto_login)
        self.firstPage.btn_createAccount.clicked.connect(self.goto_registration)

        self.loginScreen.btn_back.clicked.connect(self.goto_firstPage)
        self.loginScreen.btn_login.clicked.connect(self.goto_app)

        self.registration.btn_back.clicked.connect(self.goto_firstPage)
        self.registration.btn_register.clicked.connect(self.goto_register_firstPage)


    #we open the first screen here
        self.goto_firstPage()

        self.app.btn_decode.clicked.connect(self.onDecodeButtonClicked)
        self.app.btn_logout.clicked.connect(self.logoutButtonClicked)

    #admin buttons
        self.admin.btn_addAdmin.clicked.connect(self.onAddAdminButtonClicked)
        self.admin.btn_addItem.clicked.connect(self.onAddItemToSlownikButtonClicked)
        self.admin.btn_addDic.clicked.connect(self.onAddDictionaryButtonClicked)
        self.admin.btn_removeAdmin.clicked.connect(self.onRemoveAdminButtonClicked)
        self.admin.btn_logout.clicked.connect(self.logoutButtonClicked)
        self.admin.btn_removeDict.clicked.connect(self.removeDictionaryButtonClicked)

#functions for handling buttons
    def logoutButtonClicked(self):
        print('I logged out')
        self.setCurrentIndex(self.indexOf(self.firstPage))


    def goto_login(self):
        self.setCurrentIndex(self.indexOf(self.loginScreen))
        self.loginScreen.txtField_username.setText('')
        self.loginScreen.txtField_password.setText('')

    def goto_registration(self):
        self.setCurrentIndex(self.indexOf(self.registration))
        self.registration.txtField_email.setText('')
        self.registration.txtField_password.setText('')
        self.registration.txtField_password_2.setText('')
        self.registration.lbl_message.setText('')

    def goto_firstPage(self):
        self.setCurrentIndex(self.indexOf(self.firstPage))

    def goto_app(self):
        # TODO implement login with email

        emailL = self.loginScreen.txtField_username.text()
        passwordL = self.loginScreen.txtField_password.text()
        listaAdminow=dbConn.GetWszystkieAdminy(self.dbConn)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if emailL != '' and passwordL != '':
            if re.fullmatch(regex, emailL):
                if self.loginScreen.loginToAccount(emailL, passwordL):
                    if emailL.lower() in [l.lower() for l in listaAdminow]:
                        print('ok')
                        self.setCurrentIndex(self.indexOf(self.admin))
                        self.admin.txtField_email.setText('')
                        self.admin.lbl_output_1.setText('')
                        self.admin.lbl_output_4.setText('')
                        self.admin.txtField_word.setText('')
                        self.admin.lbl_output_2.setText('')
                        self.admin.txtField_dicName.setText('')
                        self.admin.txtField_pathToDic.setText('')
                        self.admin.lbl_output_3.setText('')
                    else:
                        self.setCurrentIndex(self.indexOf(self.app))
                        self.app.txtField_hash.setText('')
                        self.app.lbl_wynik_out.setText('')
                    print('Login success')
                else:
                    self.loginScreen.lbl_message.setText('Invalid email or password')
            else:
                self.loginScreen.lbl_message.setText('Input text in email field is not an email')
        else:
            self.loginScreen.lbl_message.setText('One or more fields are empty')


    def goto_register_firstPage(self):
        #TODO show a message or smth after login

        emailR = self.registration.txtField_email.text()
        passwordR = self.registration.txtField_password.text()
        passwordR2 = self.registration.txtField_password_2.text()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        #email validation regex from  https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

        if emailR != '' and passwordR!='' and passwordR2!='':
            if re.fullmatch(regex, emailR):
                if passwordR == passwordR2:
                    if len(passwordR) >= 6:
                        self.registration.createAnAccount(emailR, passwordR)
                    else:
                        self.registration.lbl_message.setText('Password must be a string at least 6 characters long.')
                else:
                    self.registration.lbl_message.setText('Passwords do not match')
            else:
                self.registration.lbl_message.setText('Input text in email field is not an email')
        else:
            self.registration.lbl_message.setText('One or more fields are empty')


    def onDecodeButtonClicked(self):
        algorytm=self.app.combo_algorytmy.currentText()
        metoda=self.app.combo_metody.currentText()
        slownik=self.app.combo_slowniki.currentText()
        hash=self.app.txtField_hash.text()

        if algorytm=='' or metoda=='' or (metoda=='Słownikowa' and slownik=='') or hash=='':
            self.app.lbl_wynik_out.setText('One or more fields are empty')
        else:
            self.app.onDecodeButtonClicked()


    def onAddAdminButtonClicked(self):
        inputEmail=self.admin.txtField_email.text()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # email validation regex from  https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

        if inputEmail=='':
            self.admin.lbl_output_1.setText('This field cannot be empty')
        else:
            if re.fullmatch(regex, inputEmail):
                self.admin.onAddAdminButtonClicked(inputEmail)
            else:
                self.admin.lbl_output_1.setText('This has to be email')

    def onAddItemToSlownikButtonClicked(self):
        inputSlownik=self.admin.combo_slowniki.currentText()
        inputWord=self.admin.txtField_word.text()

        if inputSlownik == '' or inputWord == '':
            self.admin.lbl_output_2.setText('One of the fields is empty')
        else:
            self.admin.onAddItemToSlownikButtonClicked(inputSlownik,inputWord)

    def onAddDictionaryButtonClicked(self):
        inputPath = self.admin.txtField_pathToDic.text()
        dictionaryName=self.admin.txtField_dicName.text()

        if inputPath == '' or dictionaryName=='':
            self.admin.lbl_output_3.setText('One of the fields is empty')
        else:
            if inputPath.endswith(".txt"):
                escaped_path = inputPath.replace('\\', '\\\\')

                print(escaped_path)
                if os.path.exists(escaped_path):
                    self.admin.onAddDictionaryButtonClicked(dictionaryName,inputPath)
                else:
                    self.admin.lbl_output_3.setText("The file does not exist")
            else:
                self.admin.lbl_output_3.setText("File has to be in txt format")

    def onRemoveAdminButtonClicked(self):
        inputAdmin = self.admin.combo_admins.currentText()

        if inputAdmin =='':
            self.admin.lbl_output_4.setText('This field cannot be empty')
        else:
            self.admin.onRemoveAdminButtonClicked(inputAdmin)

    def removeDictionaryButtonClicked(self):
        inputDictionary = self.admin.combo_deleteDict.currentText()

        if inputDictionary =='':
            self.admin.lbl_output_5.setText('This field cannot be empty')
        else:
            self.admin.removeDictionaryButtonClicked(inputDictionary)
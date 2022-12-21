import sys
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

class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):

#creating objects of all the screens so we can open them later
        super().__init__()
        self.firstPage = FirstPage()
        self.loginScreen = LoginScreen()
        self.registration = RegistrationScreen()
        self.app = App();
        self.admin = Admin();

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
        self.loginScreen.btn_login_w_gogle.clicked.connect(self.goto_app_w_gogle)

        self.registration.btn_back.clicked.connect(self.goto_firstPage)
        self.registration.btn_register.clicked.connect(self.goto_register_firstPage)

#we open the first screen here
        self.goto_firstPage()

        self.app.btn_decode.clicked.connect(self.onDecodeButtonClicked)


#functions for handling buttons
    def goto_login(self):
        self.setCurrentIndex(self.indexOf(self.loginScreen))
        self.loginScreen.txtField_username.setText('')
        self.loginScreen.txtField_password.setText('')

    def goto_registration(self):
        self.setCurrentIndex(self.indexOf(self.registration))
        self.registration.txtField_email.setText('')
        self.registration.txtField_password.setText('')
        self.registration.txtField_password_2.setText('')

    def goto_firstPage(self):
        self.setCurrentIndex(self.indexOf(self.firstPage))

    def goto_app(self):
        # TODO implement login with email

        emailL = self.loginScreen.txtField_username.text()
        passwordL = self.loginScreen.txtField_password.text()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if emailL != '' and passwordL != '':
            if re.fullmatch(regex, emailL):
                if self.loginScreen.loginToAccount(emailL, passwordL):
                    if emailL=="pekakracker@gmail.com":
                        self.setCurrentIndex(self.indexOf(self.admin))
                    else:
                        self.setCurrentIndex(self.indexOf(self.app))
                    print('Login success')
                else:
                    self.loginScreen.lbl_message.setText('Invalid email or password')
            else:
                self.loginScreen.lbl_message.setText('Input text in email field is not an email')
        else:
            self.loginScreen.lbl_message.setText('One or more fields are empty')


    def goto_app_w_gogle(self):
        #TODO implement login to app with google
        self.setCurrentIndex(self.indexOf(self.app))

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
                        temp = self.registration.createAnAccount(emailR, passwordR)
                        if temp:
                            self.registration.lbl_message.setText('Account created successfully')
                            print(emailR, ' ', passwordR, ' ', passwordR2)
                        else:
                            self.registration.lbl_message.setText('Account with this email already exists, please try to login')
                            print(emailR, ' ', passwordR, ' ', passwordR2)
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

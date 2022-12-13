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

class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):

#creating objects of all the screens so we can open them later
        super().__init__()
        self.firstPage = FirstPage()
        self.loginScreen = LoginScreen()
        self.registration = RegistrationScreen()
        self.app = App();

#adding widget so we can open them overall
        self.addWidget(self.firstPage)
        self.addWidget(self.loginScreen)
        self.addWidget(self.registration)
        self.addWidget(self.app)
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



#functions for handling buttons
    def goto_login(self):
        self.setCurrentIndex(self.indexOf(self.loginScreen))

    def goto_registration(self):
        self.setCurrentIndex(self.indexOf(self.registration))

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
                    self.setCurrentIndex(self.indexOf(self.app))
                    print('Login success')
                else:
                    print('Invalid email or password')
            else:
                print('Input text in email field is not an email')
        else:
            print('NOT OK - one or more fields are empty')


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
                        print('OK - creating account')
                        print(emailR, ' ', passwordR, ' ', passwordR2)
                        self.registration.createAnAccount(emailR,passwordR)
                        #self.setCurrentIndex(self.indexOf(self.firstPage))
                    else:
                        print('Password must be a string at least 6 characters long.')
                else:
                    print('Passwords do not match')
            else:
                print('Input text in email field is not an email')
        else:
            print('NOT OK - one or more fields are empty')


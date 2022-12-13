import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

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
        self.setCurrentIndex(self.indexOf(self.app))

    def goto_app_w_gogle(self):
        #TODO implement login to app with google
        self.setCurrentIndex(self.indexOf(self.app))

    def goto_register_firstPage(self):
        #TODO implement register account and go back to first page
        self.setCurrentIndex(self.indexOf(self.firstPage))
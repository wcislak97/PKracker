import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from globalConfigs import *

class RegistrationScreen(QDialog):
    def __init__(self):
        super(RegistrationScreen,self).__init__()
        loadUi(registrationPath,self)
        self.txtField_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtField_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        cred = credentials.Certificate(keyPath)
        firebase_admin.initialize_app(cred)

    def createAnAccount(self,email,password):
        try:
            user = auth.create_user(email=email, password=password)
            self.lbl_message.setText('Account created successfully')
        except:
            self.lbl_message.setText('Account with this email already exists, please try to login')



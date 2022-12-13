import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class RegistrationScreen(QDialog):
    def __init__(self):
        super(RegistrationScreen,self).__init__()
        loadUi("./UI/registration.ui",self)
        self.txtField_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtField_password_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def createAnAccount(self,email,password):

        cred = credentials.Certificate("pkracker-bf681-firebase-adminsdk-652ii-647b008451.json")
        firebase_admin.initialize_app(cred)
        try:
            user = auth.create_user(email=email, password=password)
        except:
            print("Email already exists")
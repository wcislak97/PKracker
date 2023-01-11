import sys
import pyrebase
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import firebase_admin
from firebase_admin import credentials
import pyrebase
from globalConfigs import *

#app specific imports

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi(loginPath,self)
        self.txtField_password.setEchoMode(QtWidgets.QLineEdit.Password)


# login with email account
    def loginToAccount(self,email,password):
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth=firebase.auth()

        try:
            login=auth.sign_in_with_email_and_password(email,password)
            return 1
        except:
            return 0
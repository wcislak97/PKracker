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

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi(adminPath, self)


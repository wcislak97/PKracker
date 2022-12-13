import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

#app specific imports

class App(QDialog):
    def __init__(self):
        super(App, self).__init__()
        loadUi("./UI/app.ui", self)

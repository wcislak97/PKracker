import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
from globalConfigs import *

class FirstPage(QDialog):
    def __init__(self):
        super(FirstPage, self).__init__()
        loadUi(firstPagePath, self)



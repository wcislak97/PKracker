import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

# #app specific imports
from mainWindow import *

app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
try:
    app.exec_()
    #sys.exit(app_exec())
except:
    print("Exiting gracefully")
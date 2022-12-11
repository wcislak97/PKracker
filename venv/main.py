import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

class loginPage(QDialog):
    def __init__(self):
        super(loginPage, self).__init__()
        loadUi("venv/first.ui", self)

#main
app = QApplication(sys.argv)
loginPageWidget = loginPage()
widget = QStackedWidget()
widget.addWidget(loginPageWidget)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")

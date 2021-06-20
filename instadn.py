# GUI
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from instagui import Ui_MainWindow

# insta
import webbrowser
import instaloader
import sys


#  code

class Main(QMainWindow):
    def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.download)
    
    def download(self):
        # insta code
        insta_id = self.ui.lineEdit.text()
        webbrowser.open(f"www.instagram.com/{insta_id}")
        mod = instaloader.Instaloader()
        mod.download_profile(insta_id, profile_pic_only = True)

        downloaded = "Profile Downloaded"
        self.ui.textBrowser.setText(downloaded)


app = QApplication(sys.argv)
insta = Main()
insta.show()
exit(app.exec_())



     


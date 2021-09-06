import sys
from PyQt4 import QtCore, QtGui, uic
from game_auto import *

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
         self.btn_start.clicked.connect(self.StartGame)
         self.btn_guess.clicked.connect(self.guess)
         self.password= ""
         
     def StartGame(self):
         self.btn_guess.setEnabled(True)
         self.btn_start.setEnabled(False)
         self.ln_guess.setEnabled(True)
         passw = self.ln_password.text()
         self.ln_password.setText("*"*len(passw))
         self.password = str(passw)
         print(self.password)

     def guess(self):
         check = self.ln_guess.text()
##         print(check)
##         print(self.password)
##         while(True):
##             if str(check)== (str(self.password)):
##                 self.ln_guess.setText("")
##                 continue
         self.ln_guess.setText("")
         print(check.type())
         
         

     
        
        
        

    
             
         


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

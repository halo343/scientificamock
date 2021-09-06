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
         self.guess = self.ln_guess.text()
         
     def StartGame(self):
         self.btn_guess.setEnabled(True)
         self.btn_start.setEnabled(False)
         self.ln_guess.setEnabled(True)
         passw = self.ln_password.text()
         self.ln_password.setText("*"*len(passw))
         self.password = str(passw)
         print(self.password)

     def guess(self):
         self.guess = str(self.ln_guess.text())
##         print(check)
##         print(self.password)
         
##             if self.checkZero() == True:
##                 print()
         if self.checkZero() == True:
              self.ln_guess.setText("")
         if self.aretherealphas() == True:
              self.ln_guess.setText("")
         if self.areThereRepeatingDigits() == True:
              self.ln_guess.setText("")
         text = self.matchingPrintDigits()
         print(text)
##         print(self.matchDigits())
         self.lb_result.setText(text)
         self.Result()
         
                 
         
         
         
     def checkZero(self):
         if self.guess[0] == "0":
             return True
         return False

     def aretherealphas(self):
         if self.guess.isdigit():
            return True
         return False
     def areThereRepeatingDigits(self):
         for i in self.guess:
            if self.guess.count(i)>1:
               return True
            return False
     def matchingPrintDigits(self):
         textFinal = ""
         for i in (self.password):
          
            if self.password.find(i)== self.guess.find(i):
               textFinal = textFinal+ "The digit"+str(i)+" is in the right position \n"
         return textFinal

     def Result(self):
        if self.guess == self.password:
            self.result.setText("Game Over. You won")
##     def matchDigits(self):
##         c=0
##         for i in self.password:
##            if self.guess.count(i)>0:
##               c=c+1
##            
##         return c
            
         

    
        
        
        

    
             
         


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

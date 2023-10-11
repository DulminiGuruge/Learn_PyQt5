from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")

"""
QComboBox -
A QComboBox widget presents a drop-down list of items for the user 
to select an option from. The advantage of this widget is that it takes 
up very little space on the screen, even if it has alot of different options. 
""" 
combo = QtWidgets.QComboBox(win)
combo.addItem("Blue")
combo.addItem("Green")
combo.addItem("Red")
combo.move(10,10)

"""

QTextEdit
Like the QLineEdit widget, QTextEdit is used to take input from the user in the 
form of text. However, unlike QLineEdit which only takes input in a single line, 
QTextEdit offers a large area where the User can input several lines of text, or 
even several paragraphs.
"""



date = QtWidgets.QTextEdit(win)
date.setFixedSize(200,100)
date.move(60,60)
 
win.show()
sys.exit(app.exec_())
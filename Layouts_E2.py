
"""
VBox layout

The QVBoxLayout is a special type of layout which arranges all the widgets inside 
it in a vertical column. The order in which you add the widgets to the layout changes 
how they appear in the PyQt window.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        Button1 = QPushButton('PyQt')
        Button2 = QPushButton('Layout')
        Button3 = QPushButton('Management')
         
        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
 
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

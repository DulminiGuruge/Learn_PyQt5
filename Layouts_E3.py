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
         
        hbox = QHBoxLayout()
        hbox.addWidget(Button1)
        hbox.addWidget(Button2)
        hbox.addWidget(Button3)
 
        self.setLayout(hbox)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

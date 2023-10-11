
"""
QGridLayout Manager
The Grid in the QGridLayout is ever expanding, and will keep increasing as you add widgets. 
The above image is just for explanatory purposes, (3, 3) isn’t a limit to it’s size or anything.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
 
        Button1 = QPushButton('Up')
        Button2 = QPushButton('Left')
        Button3 = QPushButton('Right')
        Button4 = QPushButton('Down')
         
        grid = QGridLayout()
        grid.addWidget(Button1, 0, 1)
        grid.addWidget(Button2, 1, 0)
        grid.addWidget(Button3, 1, 2)
        grid.addWidget(Button4, 1, 1)
 
        self.setLayout(grid)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('PyQt5 Layout')
        self.show()
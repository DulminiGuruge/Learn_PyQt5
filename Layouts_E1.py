"""
Absolute Positioning -
The move method takes two parameters, a X coordinate and a Y coordinate. 
Remember, the top-left hand corner has the coordinates (0,0) and they increase 
from top to bottom and left to right.
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
 
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        Button1 = QPushButton('PyQt', self)
        Button1.move(20, 10)
 
        Button2 = QPushButton('Layout', self)
        Button2.move(40, 50)
 
        Button3 = QPushButton('Management', self)
        Button3.move(60, 90)
 
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('PyQt5 Layout Management')
        self.show()
 
def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
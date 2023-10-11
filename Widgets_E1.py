from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,500,300)
    win.setWindowTitle("Daily Emails")

    """
    Label-
    creates a label object.
    Passing the window object we created (win) into 
    it’s parameters declares that the label is part of that window.
    """
    label = QtWidgets.QLabel(win) 
    label.setText("Label")
    label.adjustSize()
    label.move(10,10)

    """
     QPushButton -
     it’s a button that triggers a function when pushed
    """
    button = QtWidgets.QPushButton(win)
    button.clicked.connect(win.close)
    button.setText("Quit!")
    button.resize(60,40)
    button.move(40,40)

    """
    QLineEdit - 
    Taking input through this widget.
    Create a single line to input text
    """
    line = QtWidgets.QLineEdit(win)
    line.move(20,110)

    def show():
        print(win.text())

    """
    QRadioButton -
    Radio Buttons are commonly seen in GUI’s where the user is presented with a list of options.
    """    

    layout = QGridLayout()
 
    radio = QtWidgets.QRadioButton(win)
    radio.setText("Option1")
    radio.move(50,150)
    layout.addWidget(radio, 0, 0)
    
    radio2 = QtWidgets.QRadioButton(win)
    radio2.setText("Option2")
    radio2.move(50,180)
    layout.addWidget(radio, 0, 1)

    """
    QCheckBox - 
    A Checkbox is an important part of any GUI, used when you want to present 
    the User with a list of options. In PyQt5, we have a widget called the 
    QCheckBox which we use to create check boxes or check buttons as they
    """
    layout1 = QGridLayout()
 
    check = QtWidgets.QCheckBox(win)
    check.setText("Option1")
    check.move(50,210)
    layout1.addWidget(check, 0, 0)
    
    check2 = QtWidgets.QCheckBox(win)
    check2.setText("Option2")
    check2.move(50,240)
    layout1.addWidget(check2, 0, 1)



 
    win.show()
    sys.exit(app.exec_())
     
window() 
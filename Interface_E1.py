"""
Interface for Daily Eamil list
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,QLabel,
                             QHBoxLayout, QVBoxLayout, QGridLayout,QTextEdit,QLineEdit)
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):

        #add the title
        lbl_name = QLabel() 
        lbl_name.setText("Daily Emails")
        lbl_name.adjustSize()
        lbl_name.move(250,10)

        #text  to add emails
        txt_recepient = QLineEdit()
        
        #add recepient button
        btn_email = QPushButton('Add Email')
        btn_email.resize(60,40)
        btn_email.move(40,40)

        #vbox to add text and the button
        vbox_recepient = QVBoxLayout()
        vbox_recepient.addWidget(txt_recepient)
        vbox_recepient.addWidget(btn_email)

        #text  area to edit added emails
        txt_recepient = QTextEdit()
        txt_recepient.setFixedSize(250,200)
        txt_recepient.move(60,60)

        #edit  recepient button
        btn_email = QPushButton('Delete Email')
        btn_email.resize(60,40)
        btn_email.move(40,40)

        hbox_receipients= QHBoxLayout()
        hbox_receipients.addLayout(vbox_recepient)
        hbox_receipients.addWidget(txt_recepient)
        hbox_receipients.addWidget(btn_email)

        vbox_main = QVBoxLayout()
        vbox_main.addWidget(lbl_name)
        vbox_main.addLayout(hbox_receipients)   
        
        self.setLayout(vbox_main)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('PyQt5 Layout')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
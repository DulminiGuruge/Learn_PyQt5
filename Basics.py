from PyQt5.QtWidgets import QApplication,QLabel

app = QApplication([]) # this function is necessary to execute any PyQt window
label = QLabel('Hello World!')
label.show() 
app.exec_()
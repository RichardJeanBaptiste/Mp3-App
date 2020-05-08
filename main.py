# get url

#check if its a playlist or a clip

#choose between video/audio
    #choose extention

#choose file location

#download

import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

urlButton = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText(pyperclip.paste())
    alert.exec_()
urlButton.clicked.connect(on_button_clicked)
layout.addWidget(urlButton)
window.setLayout(layout)
window.show()
app.exec_()
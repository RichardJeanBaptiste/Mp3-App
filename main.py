# get url

#check if its a playlist or a clip

#choose between video/audio
    #choose extention

#choose file location

#download

import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QWidget
from mp3 import downloadVid

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

urlButton = QPushButton('Click')
def on_button_clicked():
    downloadVid(pyperclip.paste())

urlButton.clicked.connect(on_button_clicked)
layout.addWidget(urlButton)
window.setLayout(layout)
window.show()
app.exec_()
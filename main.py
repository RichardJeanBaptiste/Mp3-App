# get url

#check if its a playlist or a clip

#choose between video/audio
    #choose extention

#choose file location

#download

import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QComboBox, QFileDialog, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
from mp3 import downloadVid

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# enter url 
url = QLineEdit()

#choose mp3/mp4
check = QComboBox()
check.addItems(['mp3','mp4'])


# download button
downloadButton = QPushButton('Click')
def on_button_clicked():
    ext = check.currentText()
    filepath = QFileDialog.getExistingDirectory(caption="Choose Location",directory="/")
    downloadVid(url.text(), ext, filepath)
downloadButton.clicked.connect(on_button_clicked)


layout.addWidget(url)
layout.addWidget(check)
layout.addWidget(downloadButton)
window.setLayout(layout)
window.show()
app.exec_()
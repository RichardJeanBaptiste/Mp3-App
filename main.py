# get url
#check if its a playlist or a clip
#choose between video/audio
#choose extention
#choose file location
# create albums
#download

import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QFileDialog, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
from mp3 import downloadVid, downloadPlaylist

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# enter url 
url = QLineEdit()

#choose mp3/mp4
check = QComboBox()
check.addItems(['mp3','mp4'])

#playlist/checkbox
plCheck = QCheckBox("playlist")

# download button
downloadButton = QPushButton('Click')
def on_button_clicked():

    ext = check.currentText()
    filepath = QFileDialog.getExistingDirectory(caption="Choose Location",directory="/")

    if plCheck.isChecked():
        downloadPlaylist(url.text(),ext,filepath)
    else:
        downloadVid(url.text(), ext, filepath)
    
downloadButton.clicked.connect(on_button_clicked)


layout.addWidget(url)
layout.addWidget(check)
layout.addWidget(plCheck)
layout.addWidget(downloadButton)
window.setLayout(layout)
window.show()
app.exec_()
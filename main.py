# get url
#check if its a playlist or a clip
#choose between video/audio
#choose extention
#choose file location
# create albums
#download

import re
import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QButtonGroup, QCheckBox, QComboBox, QFileDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, QWidget, QWidget
from mp3 import downloadVid, downloadPlaylist, getStreams, downloadStream


class SubWindow(QWidget):
    currStream  = ''
    filepath = ''
    urlString = ''

    def __init__(self, url, streams, parent = None):
        super(SubWindow, self).__init__(parent)
        self.title = "Streams"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        SubWindow.url = url
        layout = QVBoxLayout()
        self.setLayout(layout)
        #print all the streams / set stream
        for x in streams:
            radiobutton = QRadioButton(str(x),self)
            radiobutton.format = str(x)
            layout.addWidget(radiobutton)
            radiobutton.toggled.connect(self.onClicked)
        
        downloadButton = QPushButton('Download')
        downloadButton.clicked.connect(self.onDownload)
        layout.addWidget(downloadButton)
            
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            SubWindow.currStream = radioButton.format
            
            
    # download stream
    def onDownload(self):
        downloadStream(SubWindow.url, SubWindow.currStream)
        self.close()
        
      


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #enter url
        url = QLineEdit()

        #audio/video checkbox
        audioCheck = QCheckBox('audio')
        videoCheck = QCheckBox('video')
        self.buttongroup = QButtonGroup()
        self.buttongroup.addButton(audioCheck, 2)
        self.buttongroup.addButton(videoCheck, 3)

        # download button
        downloadButton = QPushButton('Click')


        def on_button_clicked():

            filepath = QFileDialog.getExistingDirectory(caption="Choose Location",directory="/")

            if videoCheck.isChecked():
                streamList = getStreams(url.text())
                urlName = url.text()
                self.openSub(urlName,streamList)
                #downloadVid(url.text(), 'video', filepath)
            elif audioCheck.isChecked():
                downloadVid(url.text(), 'audio', filepath)

        
        downloadButton.clicked.connect(on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(url)
        layout.addWidget(audioCheck)
        layout.addWidget(videoCheck)
        layout.addWidget(downloadButton)
        self.setLayout(layout)
    
    #open second window
    def openSub(self,urlName, streamList):
        self.sub = SubWindow(urlName,streamList)
        self.sub.show()

app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec_())
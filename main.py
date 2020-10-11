# get url
#check if its a playlist or a clip
#choose between video/audio
#choose extention
#choose file location
# create albums
#download
import os
import re
import sys
from PyQt5.QtWidgets import QApplication, QButtonGroup, QCheckBox, QComboBox, QFileDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, QWidget, QWidget
from mp3 import downloadPlaylist, getStreams, downloadStream
from pathlib import Path
from playlist import playlistWindow


class SubWindow(QWidget):
    currStream  = ''
    filepath = str(os.path.join(Path.home(), "Downloads"))
    urlString = ''
    format = ''
    filePathLine = QLineEdit(placeholderText=filepath, readOnly=True)

    def __init__(self, url, streams, format, parent = None):
        super(SubWindow, self).__init__(parent)
        self.title = "Streams"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        SubWindow.url = url
        SubWindow.format = format
        layout = QVBoxLayout()
        self.setLayout(layout)

        #print all the streams / set stream
        for x in streams:
            radiobutton = QRadioButton(str(x),self)
            radiobutton.format = str(x)
            layout.addWidget(radiobutton)
            radiobutton.toggled.connect(self.onClicked)
        
        line = QHBoxLayout()
        line.addWidget(SubWindow.filePathLine)
        locationButton = QPushButton('Change Directory')
        locationButton.clicked.connect(self.changeLocation)
        line.addWidget(locationButton)
        
        downloadButton = QPushButton('Download')
        downloadButton.clicked.connect(self.onDownload)
        layout.addLayout(line)
        layout.addWidget(downloadButton)
            
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            SubWindow.currStream = radioButton.format
    
    # change file location
    def changeLocation(self):
        filepath = QFileDialog.getExistingDirectory(caption="Choose Location",directory=SubWindow.filepath)
        SubWindow.filepath = filepath
        SubWindow.filePathLine.setText(filepath)
        
             
    # download stream
    def onDownload(self):
        downloadStream(SubWindow.url, SubWindow.filepath, SubWindow.currStream, SubWindow.format)
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
        
        formatButtons = QHBoxLayout()
        formatButtons.addWidget(audioCheck)
        formatButtons.addWidget(videoCheck)

        #playlist checkbox
        playlistCheck = QCheckBox('playlist')
        
        # download button
        downloadButton = QPushButton('Click')

        def on_button_clicked():
            urlName = url.text()

            if(playlistCheck.isChecked()):
                try:
                    self.openPlaylist(urlName)
                except ValueError:
                    alert = QMessageBox()
                    alert.setText('Enter a valid url')
                    alert.exec_()
                return

            if videoCheck.isChecked():
                try:
                    streamList = getStreams(url.text(), 'video')
                    self.openSub(urlName,streamList, 'video')
                except TypeError:
                    pass
            elif audioCheck.isChecked():
                try:
                    streamList = getStreams(url.text(), 'audio')
                    self.openSub(urlName,streamList, 'audio')
                except TypeError:
                    pass
                

        downloadButton.clicked.connect(on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(url)
        layout.addLayout(formatButtons)
        layout.addWidget(playlistCheck)
        layout.addWidget(downloadButton)
        self.setLayout(layout)
    
    #open second window
    def openSub(self,urlName, streamList, format):
        self.sub = SubWindow(urlName,streamList, format)
        self.sub.show()
    
    def openPlaylist(self,url):
        self.sub = playlistWindow(url)
        self.sub.show()


app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec_())
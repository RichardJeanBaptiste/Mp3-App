from PyQt5.QtWidgets import *
from pathlib import Path
from mp3 import downloadPlaylist
import pafy
import os
import sys


class playlistWindow(QWidget):

    urlstring = ''
    ext = ''
    albumName = ''
    albumArtist = ''
    filepath = str(os.path.join(Path.home(), "Downloads"))
    filePathLine = QLineEdit(placeholderText=filepath, readOnly=True)

    def __init__(self, url, parent = None):
        super(playlistWindow, self).__init__(parent)
        self.title = "playlist download"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        playlistWindow.urlstring = url
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Set Meta Tag Names')
        AlbumName = QLineEdit("Set album name")
        AlbumArtist = QLineEdit("Set artist name")
        AlbumName.textChanged.connect(self.albumNameChange)
        AlbumArtist.textChanged.connect(self.albumArtistChange)

        # ext
        combo = QComboBox()
        combo.addItem("mp3")
        combo.addItem("mp4")
        combo.activated[str].connect(self.onChanged)

        # filepath
        line = QHBoxLayout()
        line.addWidget(playlistWindow.filePathLine)
        locationButton = QPushButton('Change Directory')
        locationButton.clicked.connect(self.changeLocation)
        line.addWidget(locationButton)
        
        
        
        downloadButton = QPushButton('Download')
        downloadButton.clicked.connect(self.onDownload)

        layout.addWidget(label)
        layout.addWidget(AlbumName)
        layout.addWidget(AlbumArtist)
        layout.addWidget(combo)
        layout.addLayout(line)
        layout.addWidget(downloadButton)
    
    # change file location
    def changeLocation(self):
        filepath = QFileDialog.getExistingDirectory(caption="Choose Location",directory=playlistWindow.filepath)
        playlistWindow.filepath = filepath
        playlistWindow.filePathLine.setText(filepath)
    
    def onChanged(self,text):
        playlistWindow.ext = text

    def albumNameChange(self,text):
        playlistWindow.albumName = text
    
    def albumArtistChange(self,text):
        playlistWindow.albumArtist = text
    
    # download stream
    def onDownload(self):
        downloadPlaylist(playlistWindow.urlstring,playlistWindow.ext,playlistWindow.filepath)
        self.close()
            
    
app = QApplication([])
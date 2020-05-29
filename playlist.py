from PyQt5.QtWidgets import *
import pafy
from pathlib import Path


class playlistWindow(QWidget):
    
    def __init__(self, parent = None):
        super(playlistWindow, self).__init__(parent)
        self.title = "playlist download"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Set Meta Tag Names / Optional*')
        AlbumName = QLineEdit("Set album name")
        AlbumArtist = QLineEdit("Set artisit name")
        
        downloadButton = QPushButton('Download')
        layout.addWidget(label)
        layout.addWidget(AlbumName)
        layout.addWidget(AlbumArtist)
        layout.addWidget(downloadButton)
            
    
app = QApplication([])
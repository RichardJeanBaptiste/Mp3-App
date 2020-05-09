from mp3_tagger import MP3File
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget
import pafy
import os

app = QApplication([])

# open a window
# show url details
# choose download location
# choose between video/audio
# download

def downloadVid(url, ext, filepath):
    try:
        video = pafy.new(url)
        if(ext == 'mp4'):
            best = video.getbest()
            best.download(filepath=filepath)
        else:
            best = video.getbestaudio()
            best.download(filepath=filepath)
        
    except ValueError:
        alert = QMessageBox()
        alert.setText('Enter a valid url')
        alert.exec_()



'''
plurl = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOsxT6cdEgVpBV-rijwjbbs3"
playlist = pafy.get_playlist(plurl)


for x in range(len(playlist)):
    print(playlist['items'][x]['pafy'])
    playlist['items'][x]['pafy'].getbestaudio().download(filepath="tmp")
 
urls = os.listdir("tmp")

def changeTags(x):
    print(x)
    mp3 = MP3File(x)
    mp3.album = 'Love Me Dearly'
    mp3.artist = 'Ivory Wade'
    mp3.save()


for x in urls:
    x = "tmp/" + x
    changeTags(x)
'''
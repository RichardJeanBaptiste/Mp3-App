from mp3_tagger import MP3File
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QWidget
import pafy
import os

app = QApplication([])

def downloadVid(url):
    try:
        video = pafy.new(url)
        best = video.getbest()
        best.download()
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
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


def getStreams(url):
    streamArray = []
    video = pafy.new(url)
    streams = video.videostreams
    for s in streams:
        streamArray.append(s)
    streamArray = reversed(streamArray)
    return streamArray


def downloadStream(url, filepath, streamName):
    video = pafy.new(url)
    streams = video.videostreams
    for i in range(len(streams)):
        if(str(streams[i]) == streamName):
            video.videostreams[i].download(filepath=filepath)
    
    
        
def downloadVid(url, ext, filepath):
    try:
        video = pafy.new(url)
        if(ext == 'video'):
            best = video.getbest()
            best.download(filepath=filepath)
        else:
            best = video.getbestaudio()
            best.download(filepath=filepath)
        
    except ValueError:
        alert = QMessageBox()
        alert.setText('Enter a valid url')
        alert.exec_()


def downloadPlaylist(url,ext,filepath):
    try:
        plurl = url
        playlist = pafy.get_playlist(plurl)
        if(ext == 'mp4'):
            for x in range(len(playlist)):
                try:
                   playlist['items'][x]['pafy'].getbestvideo().download(filepath=filepath)
                except OSError:
                    print('no video formats found...try again')
        else:
            for x in range(len(playlist)):
                try:
                   playlist['items'][x]['pafy'].getbestaudio().download(filepath=filepath)
                except OSError:
                    print('no video formats found...try again')
    except ValueError:
        alert = QMessageBox()
        alert.setText('Enter a valid url')
        alert.exec_()

'''
plurl = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOsxT6cdEgVpBV-rijwjbbs3"
playlist = pafy.get_playlist(plurl)


for x in range(len(playlist)):
    try:
        print(playlist['items'][x]['pafy'])
        playlist['items'][x]['pafy'].getbestaudio().download(filepath="tmp")
    except OSError:
        print('no video formats found...try again')
    



urls = os.listdir("tmp")

count = 0

os.chdir("/Users/Richard/Desktop/mp3-api/tmp")

for x in urls:
    a = os.path.abspath(x)
    count = count + 1
    string = "ffmpeg -i '{curr}' {output}.mp3"
    string = string.format(curr=a,output=count)
    os.system(string)

os.chdir("/Users/Richard/Desktop/mp3-api/")
urlsb = os.listdir("tmp")

def changeTags(x):
    try:
       print(x)
       mp3 = MP3File(x)
       mp3.album = 'Love Me Dearly'
       mp3.artist = 'Ivory Wade'
       mp3.save()
    except:
        pass
    


for x in urlsb:
    print(x)
'''
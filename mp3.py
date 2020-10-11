from mp3_tagger import MP3File
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget
import ffmpeg
import pafy
import os
import re

app = QApplication([])

# open a window
# show url details
# choose download location
# choose between video/audio
# download

def getStreams(url, x):
    try:
        streamArray = []
        video = pafy.new(url)
        if(x == 'video'):
            streams = video.videostreams
            for s in streams:
                streamArray.append(s)
            streamArray = reversed(streamArray)
            return streamArray
        else:
            streams = video.audiostreams
            for s in streams:
                streamArray.append(s)
            streamArray = reversed(streamArray)
            return streamArray
    except ValueError:
        alert = QMessageBox()
        alert.setText('Enter a valid url')
        alert.exec_()

    
def downloadStream(url, filepath, streamName, format):
    video = pafy.new(url)
    
    if(format == video):
        streams = video.videostreams
        for i in range(len(streams)):
            if(str(streams[i]) == streamName):
                video.videostreams[i].download(filepath=filepath)
    else:
        streams = video.audiostreams
        for i in range(len(streams)):
            if(str(streams[i]) == streamName):
                video.audiostreams[i].download(filepath=filepath)

def downloadPlaylist(url,ext,filepath):
    try:
        plurl = url
        playlist = pafy.get_playlist(plurl)
        if(ext == 'mp4'):
            for x in range(len(playlist)):
                try:
                   playlist['items'][x]['pafy'].getbestvideo().download(filepath="tmp")
                except OSError:
                    print('no video formats found...try again')
                except IndexError:
                    pass
        else:
            for x in range(len(playlist) - 1):
                try:
                   playlist['items'][x]['pafy'].getbestaudio().download(filepath="tmp")
                except OSError:
                    print('no video formats found...try again')
                except IndexError:
                    pass
    except ValueError:
        alert = QMessageBox()
        alert.setText('Enter a valid url')
        alert.exec_()

def changeTags(artist,album,filepath):
    #os.chdir("/Users/Richard/Documents/Projects/mp3-api/")
    urls = os.listdir("tmp")
    
    print(filepath)
    try:
        for x in urls:
            newPath = filepath + "/" + x[:-5] + ".mp3"
            songPath = filepath + "/" + x
            stream = ffmpeg.input(songPath)
            stream = ffmpeg.output(stream, newPath)
            ffmpeg.run(stream)
            mp3 = MP3File(newPath)
            mp3.artist = artist
            mp3.album = album
            mp3.save()
            os.remove(songPath)
    except Exception as e:
        print(e)
        pass





'''
plurl = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOtotXGiOBUjigHFNnDtgue3"
playlist = pafy.get_playlist(plurl)


for x in range(len(playlist) - 1):
    try:
        #print(playlist['items'][x]['pafy'].title)
        playlist['items'][x]['pafy'].getbestaudio().download(filepath="tmp")
        #cwd = os.getcwd()
    except OSError:
        print('no video formats found...try again')
    except IndexError:
        pass


urls = os.listdir("tmp")
os.chdir("/Users/Richard/Documents/Projects/mp3-api/tmp")

for x in urls:
    asd = os.path.splitext(x)
    songTitle = asd[0]
    extension = asd[1]

    regex = re.compile('[^a-zA-Z]')
    newName = regex.sub('', asd[0])

    newFilename = newName + asd[1]
    os.rename(x,newFilename)

    try:
        a = os.getcwd() + "/" + newFilename
        string = "ffmpeg -i {curr}  '{output}'.mp3"
        string = string.format(curr=a,output=songTitle)
        os.system(string)
    except Exception:
        pass
'''
        
'''
os.chdir("/Users/Richard/Documents/Projects/mp3-api/tmp")
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
    changeTags(x)
'''
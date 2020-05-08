from mp3_tagger import MP3File
import pafy
import os



plurl = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOsxT6cdEgVpBV-rijwjbbs3"
playlist = pafy.get_playlist(plurl)


for x in range(len(playlist)):
    print(playlist['items'][x]['pafy'])
    playlist['items'][x]['pafy'].getbestaudio(preftype="m4a").download(filepath="tmp")
 
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
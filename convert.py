import os
import pyperclip
import re


#print(pyperclip.paste())
#string = "ffmpeg -i /Users/Richard/Desktop/mp3-api/tmp/'Ivory Wade - Chill With You ft. Whodie Slim [Love Me Dearly]'.m4a output.mp3"

#os.system(string)

txt = "https://www.youtube.com/playlist?list=PLPRWtKgY2MOtt1GQCYBJviLbSaOFW1OHE"
x = re.search("(/playlist?)", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

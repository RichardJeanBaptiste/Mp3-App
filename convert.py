import os
import pyperclip
import re
import pafy


#print(pyperclip.paste())
#string = "ffmpeg -i /Users/Richard/Desktop/mp3-api/tmp/'Ivory Wade - Chill With You ft. Whodie Slim [Love Me Dearly]'.m4a output.mp3"

#os.system(string)

patt = "list="
url = "https://www.youtube.com/playlist?list=PLBOh8f9FoHHjOz0vGrD20WcTtJar-LOrw"

x = re.search(patt, url)

if x:
  print("match")
else:
  print("No match")
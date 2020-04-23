import os
fileType = '.mp3'

anyFile = os.listdir('c:/Users/vlbha/Desktop/iTunes/Songs')
for file in anyFile :
    if file.endswith(fileType):
        print(file)
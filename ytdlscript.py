import subprocess
import sys
import os
import time

def sortlength(e):
    return len(e)

if len(sys.argv) != 2:
    print("Usage: python ytdlscript <yt link>")
    exit()

ytlink = sys.argv[1]

ytdlcommand = f"youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail -f mp4 -o C:/users/seong/archive/public/videos/%(title)s.%(ext)s {ytlink}"

download = subprocess.run(ytdlcommand, check=True)


FILES_EXIST = True
while FILES_EXIST:
    print("starting while loop")
    filelist = os.listdir('.')
    sortedfilelist = [i for i in filelist if os.path.isfile(i)]
    sortedfilelist.sort(key=sortlength)
    if len(sortedfilelist) == 0:
        FILES_EXIST = False
        print("no more individual files left, exiting")
        exit()
    filename = sortedfilelist[0]
    print(filename)

    filenamewithoutext = os.path.basename(filename).split('.')[0]
    print(filenamewithoutext)

    mkdirpath = f"C:/users/seong/archive/public/videos/{filenamewithoutext}"

    if not os.path.isdir(mkdirpath):
        os.mkdir(mkdirpath)
        print("made dir")
        time.sleep(2)

        tobemovedlist = os.listdir('.')
        print(tobemovedlist)
        sortedtobemovedlist = [i for i in tobemovedlist if i.startswith(filenamewithoutext) and os.path.isfile(i)]
        sortedtobemovedlist.sort(key=sortlength)
        print(sortedtobemovedlist)


        for file in sortedtobemovedlist:
            print(file)
            print("starting for loop")
            time.sleep(2)
            destpath = f"C:/users/seong/archive/public/videos/{filenamewithoutext}/{file}"
            os.rename("C:/users/seong/archive/public/videos/" + file, destpath)
            print("moved file")

    else:
        removefilelist = os.listdir('.')
        sortedremovefilelist = [i for i in removefilelist if filenamewithoutext in i and os.path.isfile(i)]
        for j in sortedremovefilelist:
            time.sleep(2)
            os.remove(j)
            print("removed file")

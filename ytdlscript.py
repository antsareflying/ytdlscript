import subprocess
import sys
import os

def sortlength(e):
    return len(e)

if len(sys.argv) != 2:
    print("Usage: python ytdlscript <yt link>")
    exit()

ytlink = sys.argv[1]

ytdl_command = f"yt-dlp --write-description --write-info-json --write-annotations --write-sub --write-thumbnail --download-archive downloadedarchive.txt -f mp4 -o C:/users/seong/archive/public/videos/%(title)s.%(ext)s {ytlink}"

download = subprocess.run(ytdl_command, check=True)


FILES_EXIST = True
while FILES_EXIST:
    print("starting while loop")
    filelist = os.listdir('C:/users/seong/archive/public/videos')
    sortedfilelist = [i for i in filelist if os.path.isfile(i) and i is not "downloadedarchive.txt"]
    sortedfilelist.sort(key=sortlength)
    if len(sortedfilelist) == 1 and sortedfilelist[0] == "downloadedarchive.txt":
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

        tobemovedlist = os.listdir('C:/users/seong/archive/public/videos')
        print(tobemovedlist)
        sortedtobemovedlist = [i for i in tobemovedlist if i.startswith(filenamewithoutext) and os.path.isfile(i) and i is not "downloadedarchive.txt"]
        sortedtobemovedlist.sort(key=sortlength)
        print(sortedtobemovedlist)


        for file in sortedtobemovedlist:
            if file is "donwnloadedarchive.txt":
                break
            print(file)
            print("starting for loop")
            destpath = f"C:/users/seong/archive/public/videos/{filenamewithoutext}/{file}"
            os.rename("C:/users/seong/archive/public/videos/" + file, destpath)
            print("moved file")

    else:
        removefilelist = os.listdir('C:/users/seong/archive/public/videos')
        sortedremovefilelist = [i for i in removefilelist if filenamewithoutext in i and os.path.isfile(i) and i is not "downloadedarchive.txt"]
        for j in sortedremovefilelist:
            os.remove(j)
            print("removed file")
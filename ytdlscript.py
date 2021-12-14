"""
MIT License

Copyright (c) 2021 Moon Seongmu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import subprocess
import sys
import os

def sortlength(e):
    return len(e)

if len(sys.argv) != 2:
    print("Usage: python ytdlscript <yt link>")
    sys.exit()


if os.getcwd() != "C:\\Users\\seong\\archive\\public\\videos":
    print("not in public videos directory")
    sys.exit()

ytlink = sys.argv[1]

ytdl_command = f"yt-dlp --write-description --write-info-json --write-annotations --write-sub --sub-langs en --write-thumbnail --write-comments --no-playlist --verbose --download-archive C:/users/seong/archive/public/videos/downloadedarchive.txt -a C:/users/seong/archive/public/videos/downloadlinks.txt -f bv*+ba/b --merge-output-format mkv -o \"C:/users/seong/archive/public/videos/NA-%(playlist_title)s-%(playlist_id)s/%(upload_date)s-%(title)s-%(id)s/%(upload_date)s-%(title)s-%(id)s.%(ext)s\" {ytlink}"

subprocess.run(ytdl_command, check=True)



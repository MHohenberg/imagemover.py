#!/usr/bin/python

import glob, os, re, sys

def movePictures(keyword):

    # Make sure target directory exists
    try:
        os.stat(keyword)
    except:
        os.mkdir(keyword)
    
    for file in os.listdir("."):
        if re.match(keyword+".*\.[a-z].*", file):
            newfile = file.replace(keyword,"").strip()
            print file +" -> ./"+keyword+"/"+newfile

            os.rename(file, "./"+keyword+"/"+newfile)
    return

if (len(sys.argv) > 1):
    movePictures(sys.argv[1])
else:
    print "Moves files into a subdirectory based on keyword."
    print "Example: keyword filename.jpg -> ./keyword/filename.jpg"
    print "Usage: imagemover.py [KEYWORD]"

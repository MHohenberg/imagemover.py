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
    if (sys.argv[1] == '-d'):

        workedOn = []

        inf = os.walk('.')
        for x in inf:
            subfolder = x[0][2:]
            try:
                subfolder = subfolder[:subfolder.index('/',0)]
            except:
                subfolder = subfolder

            if subfolder != "":
                if not subfolder in workedOn:
                    workedOn.append(subfolder)
                    print "Arbeite an: "+subfolder
                    movePictures(subfolder)
    else:
        movePictures(sys.argv[1])
else:
    print "Moves files into a subdirectory based on keyword."
    print "Example: keyword filename.jpg -> ./keyword/filename.jpg"
    print "Usage: imagemover.py [-d|KEYWORD]"
    print "Parameters:   "
    print "     -d     Instead of a KEYWORD, uses existing directory names as keywords"

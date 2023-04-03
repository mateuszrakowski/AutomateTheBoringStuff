# unneededFiles.py - Searching through given directory and finds files with more than 100 MB of size

import os


def filesFinder(directory):
    # Get absolute path of the given dir
    directory = os.path.abspath(directory)

    for foldername, subfolders, filenames in os.walk(directory):
        # Search subfolders
        for subfolder in subfolders:
            subfolderPath = os.path.join(foldername, subfolder)
            sizeSubfolder = os.path.getsize(subfolderPath) / 1000000
            if sizeSubfolder > 100:
                print(subfolderPath)

        # Search files
        for filename in filenames:
            filenamePath = os.path.join(foldername, filename)
            sizeFilenameMB = os.path.getsize(filenamePath) / 1000000
            if sizeFilenameMB > 100:
                print(filenamePath)

filesFinder("/Users/mateuszrakowski/Downloads")

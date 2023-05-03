'''
Searches every folder on hard drive and finds potential photo folders under certain rules.

Usage:
python3 findPhotoFolders.py
'''

import os
from PIL import Image


# Search every directory in provided disk path
for directory, subdirectory, filenames in os.walk("/Users"):
    # Store number of files, reset every directory
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    fileFormats = ["jpg", ".png"]

    # Track number of files based on file format 
    for filename in filenames:
        if not filename[-4:].lower() in fileFormats:
            numNonPhotoFiles += 1
            continue

        # Try to open and retrieve size of image
        try:
            im = Image.open(os.path.join(directory, filename))
            width, height = im.size
        except:
            continue

        # Track only images which are likely photos
        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1
    
    # Return path if most files are photos
    if numPhotoFiles > numNonPhotoFiles:
        print(f"Directory with photos: {directory}")

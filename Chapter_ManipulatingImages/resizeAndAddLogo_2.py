'''
Resizes all images in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right corner. Updated version with additional features, eg. allowed additional file extensions.

Usage:
python3 resizeAndAddLogo.py
'''

import os
from PIL import Image


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs("withLogo", exist_ok=True)
fileFormats = [".png", ".jpg", ".gif", ".bmp"]

# Loop over all files in the working directory
for filename in os.listdir("."):
    if (not filename[-4:].lower() in fileFormats) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # The image must be at least twice the width and height of the logo image
    if width < (logoWidth * 2) or height < (logoHeight * 2):
        print("Image is to small to add logo.")
        continue

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # Resize the image
        print(f"Resizing {filename}")
        im = im.resize((width, height))

    # Add the logo
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes
    im.save(os.path.join("withLogo", filename))

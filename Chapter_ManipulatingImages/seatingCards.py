'''
Create images custom seating cards from a list of guests in a plaintext file.

Usage:
python3 seatingCards.py
'''

import os
from PIL import Image, ImageDraw, ImageFont


# Paths to decoration image and list with guests
DECORATION_IMG = "flowers.png"
GUEST_LIST = "guests.txt"

# Retrieve decoration image size
flowerImage = Image.open(DECORATION_IMG)
flowerWidth, flowerHeight = flowerImage.size

# Save seating cards inside directory
os.makedirs("seating_cards", exist_ok=True)

# Create invidual card for each guest on the list
with open("guests.txt", "r") as txtFile:
    for guest in txtFile:
        # Create new card
        card = Image.new("RGBA", (288, 360), "white")
        draw = ImageDraw.Draw(card)

        # Define font in variable
        fontsFolder = "/Library/Fonts"
        arialFont = ImageFont.truetype(os.path.join(fontsFolder, "Arial Unicode.ttf"), 28)

        # Create decoration on card and paste flowers image
        draw.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill="black")
        draw.text((70, 80), guest, fill="black", font=arialFont)
        card.paste(flowerImage, (0, 360 - flowerHeight), flowerImage)

        # Save each card
        card.save(os.path.join("seating_cards", guest.rstrip()) + ".png")

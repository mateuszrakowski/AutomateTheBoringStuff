''' 
imageDownloader.py - Downloads images from given search phrase
Usage: imageDownloader.py <web address> <search phrase>
'''

import sys, os, requests, bs4


# Check CLI arguments
if len(sys.argv) < 3:
    sys.exit("Too few number of arguments!")
else:
    # Save web address and search phrase to variables
    webAddress = sys.argv[1]
    searchPhrase = " ".join(sys.argv[2:])

# Create search phrase URL
webAddress = "https://" + webAddress + "/search?q=" + searchPhrase

# Open search URL results
try:
    res = requests.get(webAddress)
    res.raise_for_status()
except Exception:
    sys.exit("Can't establish connection to website.")

soup = bs4.BeautifulSoup(res.text, "html.parser")

# Possible images extensions
extensions = [".png", ".jpg", ".jpeg"]

# Create directory to store images
os.makedirs(f"{searchPhrase} images", exist_ok=True)

# Find images
imgList = soup.find_all("img")

# Limit and track number of found images
foundImgNumber = 0

if imgList == []:
    sys.exit("Couldn't find images.")

for image in imgList:
    # Get 'src' value
    imgLink = image.get("src")
    
    # Limit number of images to download
    if foundImgNumber > 5:
        break

    # Check if extension matches
    for ext in extensions:
        if imgLink.endswith(ext):
            # Create complete image link
            imgLink = "https:" + imgLink
            res = requests.get(imgLink)

            # Save images to the file inside created directory
            print(f"Downloading {imgLink}...")
            imageFile = open(os.path.join(f"{searchPhrase} images", os.path.basename(imgLink)), "wb")

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            # Track number of downloaded images
            foundImgNumber += 1

"""
Downloads XKCD comics using multiple threads.

Usage:
python3 multithreadedDownloader.py
"""

import requests, os, bs4, threading


os.makedirs("xkcd", exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print(f"Downloading page https://xkcd.com/{urlNumber}...")
        res = requests.get(f"http://xkcd.com/{urlNumber}")
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # Find the URL of the comic image
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image.")
        else:
            comicUrl = comicElem[0].get("src")
            # Download the image
            print(f"Downloading image {comicUrl}...")
            res = requests.get("https:" + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start the Thread objects
downloadThreads = []

# Loop 14 times, creates 14 threads
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        # There is no comic 0, so set it to 1
        start = 1
    
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")

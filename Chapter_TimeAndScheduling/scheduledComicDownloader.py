"""
Program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit.

Usage:
python scheduledComicDownloader.py
"""

import requests, bs4, re, threading
from pathlib import Path


# Dictionary to store URLs and CSS attribute
comicData = {
    "https://xkcd.com": "#comic img",
    "https://lefthandedtoons.com": ".comicimage",
    "https://moonbeard.com": "#comic-1 img",
}


def main():
    downloadThreads = []

    # Create and run script in multiple threads
    for url, attr in comicData.items():
        imgUrl = findComic(url, attr)
        downloadThread = threading.Thread(target=downloadComic, args=(imgUrl,))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    for downloadThread in downloadThreads:
        downloadThread.join()
    print("Done.")


def findComic(url, attribute):
    """
    Searches the page for newest added comic, checks if it is already downloaded.

    Returns:
    str: Comic image URL or information.
    """

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    comicObj = soup.select(attribute)

    if comicObj == []:
        return "Could not find comic image."
    else:
        comicImg = comicObj[0].get("src")
        return comicImg


def downloadComic(comicUrl):
    """
    Creates directory with sitename and downloads newest comic image.

    Returns:
    str: Information about success or pass.
    """

    # Modifies the URL based on extracted string from "src" attribute
    if comicUrl.startswith("https:") or comicUrl.startswith("http:"):
        res = requests.get(comicUrl)
    else:
        res = requests.get("https:" + comicUrl)
    res.raise_for_status()

    # Extracts sitename to create directory and save file
    r = re.search(r"(\w+)\.c", comicUrl)
    sitename = r.group(1)

    p = Path(sitename)
    p.mkdir(exist_ok=True)
    filePath = Path(p / Path(comicUrl).name)

    if filePath.is_file() == True:
        return f"There's no new comics on {sitename}."

    with open(filePath, "wb") as comicImg:
        for chunk in res.iter_content(100000):
            comicImg.write(chunk)
    return f"Succesfully downloaded new comic to '{str(filePath)}'!"


if __name__ == "__main__":
    main()

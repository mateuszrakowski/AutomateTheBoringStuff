"""
Searches for emotes and downloads them to directory from site 7tv.app.

Usage:
python3 emotesDownload.py
"""

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import requests, os


def findEmotes():
    '''
    Extracts each emote name and its corresponding ID, saves the data to dictionary for further URL creation. 

    Returns:
    dict: Data with collected emote name and its corresponding ID.
    '''
    options = EdgeOptions()
    website = webdriver.Edge(options=options)
    website.get("https://7tv.app/emote-sets/610f1295d86cd785a4739571")
    emotesIds = {}

    divId = WebDriverWait(website, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="emote-card-wrapper"]')))
    pageSource = website.page_source
    soup = BeautifulSoup(pageSource, "html.parser")

    for element in soup.find_all("div", class_="emote-card-wrapper"):
        id = element.get("emote-id")
        emoteName = element.find("div", class_="title-banner").find("span")
        if emoteName.get("class"):
            continue
        emotesIds[emoteName.text] = id

    return emotesIds


def downloadEmotes(emotesIds):
    '''
    Builds URLs and downloads emotes with proper file extension to created directory.

    Returns:
    list: Names of emotes that couldn't be downloaded.
    '''
    dir = os.makedirs("7tv_emotes", exist_ok=True)
    failedFiles = []
        
    for name, id in emotesIds.items():
        url = "https://7tv.app/emotes/" + id
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        largeEmote = soup.find("meta", attrs={"name": "og:image"})

        try:
            imgSrc = largeEmote.get("content")
        except:
            failedFiles.append(name)
            continue
    
        imgUrl = "https:" + imgSrc
        res = requests.get(imgUrl, stream=True)
        res.raise_for_status()
        
        fileExtension = imgSrc[-4:]
        fileName = name + fileExtension
        path = os.path.join("7tv_emotes", fileName)
            
        if os.path.exists(path):
            continue
        else:
            print(f"Downloading emote: {name}...")
            with(open(path, "wb")) as imageFile:
                imageFile.write(res.content)

    print(f"Not downloaded emotes: {failedFiles}")
        

if __name__ == "__main__":
    downloadEmotes(findEmotes())

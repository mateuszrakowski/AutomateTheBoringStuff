# game2048.py - Program that automatically plays the web game called 2048

import requests, sys, bs4, time
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = EdgeOptions()

# Initiate and open game website
browser = webdriver.Edge(options=options)
browser.get("https://play2048.co")

# Close cookies window
browser.find_element(By.ID, "ez-accept-all").click()

browser.implicitly_wait(5)

# Find body DOM element and exit point
htmlElem = browser.find_element(By.TAG_NAME, "body")
exit = browser.find_element(By.CLASS_NAME, "game-message")

# Play the game, stop when "game over" text is present
while exit.text == "":
    htmlElem.send_keys(Keys.UP)
    time.sleep(0.1)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(0.1)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(0.1)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(0.1)

# Print out result with score
score = browser.find_element(By.CLASS_NAME, "score-container")
print(f"The game is done! Your score: {score.text}.")
time.sleep(5)

browser.quit()
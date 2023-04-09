'''
cliEmailer.py - Sends message from given email address to provided address.
Usage: cliEmailer.py <email address> <message text>
'''

import sys
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By


# Check CLI arguments
if len(sys.argv) < 3:
    sys.exit("Invalid number of arguments!")
# Save arguments to corresponding variables
else:
    emailAddress = sys.argv[1]
    emailMessage = " ".join(sys.argv[2:])

# Get authorization informations
userUsername = pyip.inputStr("Username:\n")
userPassword = pyip.inputPassword("Password:\n")

# Get title
emailTitle = pyip.inputStr("Email title:\n")

# Open email website
options = EdgeOptions()

# Option that doesn't close browser after script finishes
# options.add_experimental_option("detach", True)

website = webdriver.Edge(options=options)
website.get("https://mail.google.com/mail/")

# Fill username field
usernameField = website.find_element(By.ID, "identifierId")
usernameField.send_keys(userUsername)

# Move to next page
nextButton = website.find_element(By.ID, "identifierNext")
nextButton.click()

website.implicitly_wait(5)

# Fill password field
passwordField = website.find_element(By.NAME, "Passwd")
passwordField.send_keys(userPassword)

# Move to next page
nextButton = website.find_element(By.ID, "passwordNext")
nextButton.click()

# Open new message
messageButton = website.find_element(By.CSS_SELECTOR, 
"body > div:nth-child(19) > div.nH > div > div.nH.aqk.aql.bkL > div.aeN.WR.nH.oy8Mbf > div.aic > div > div")
messageButton.click()

# Fill email address field
addressField = website.find_element(By.CSS_SELECTOR, 'input[class="agP aFw"]')
addressField.send_keys(emailAddress)

# Fill subject field
subjectField = website.find_element(By.NAME, "subjectbox")
subjectField.send_keys(emailTitle)

# Fill email message field
messageField = website.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
messageField.send_keys(emailMessage)

# Send message
sendButton = website.find_element(By.CSS_SELECTOR, 'div[class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
sendButton.click()

# Print result
print(f"Succesfully send message: {emailMessage} to {emailAddress}.")

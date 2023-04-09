from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By


options = EdgeOptions()

# Option that doesn't close browser after script finishes
# options.add_experimental_option("detach", True)

browser = webdriver.Edge(options=options)
browser.get("https://login.metafilter.com")
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('your_usename')

passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('your_password')
passwordElem.submit()

browser.quit()
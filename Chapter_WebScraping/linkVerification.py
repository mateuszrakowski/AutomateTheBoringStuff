# linkVerification.py - Searches for all link on page and checks if they work


import sys, requests, bs4


if len(sys.argv) == 2:
    websiteAddress = sys.argv[1]
else:
    sys.exit("Wrong number of arguments.")

try:
    res = requests.get(websiteAddress)
    res.raise_for_status()
except Exception:
    sys.exit("Can't establish connection to website.")

soup = bs4.BeautifulSoup(res.text, "html.parser")

valid, invalid = 0, 0

for link in soup.find_all("a"):
    checkLink = link.get("href")

    if checkLink == None:
        break
        
    if checkLink.startswith("https://"):
        res = requests.get(checkLink)
        if res.status_code == requests.codes.ok:
            print(f"VALID: {checkLink}")
            valid += 1
        else:
            print(f"INVALID: {checkLink}")
            invalid += 1

print(f"Total links: {valid + invalid}\nValid links: {valid}\nInvalid links: {invalid}")

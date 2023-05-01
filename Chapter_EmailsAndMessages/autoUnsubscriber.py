'''
Scans through email account, finds all the unsubscribe links in all emails, and automatically opens them in a browser.

Usage:
python3 autoUnsubscriber.py <gmail email address> <password>
'''

from bs4 import BeautifulSoup
import imapclient, sys, webbrowser, email
import datetime


if len(sys.argv) != 3:
    sys.exit("Invalid number of arguments.")


def findUrls():
    '''
    Finds unique URLs reffering to unsubscribe page and save them to dictionary, which protects data to contain multiple links from one subscription sender.

    Returns:
    dict: Data with collected information about sender and link to unsubscribe.
    '''

    # Create IMAP object and log in to email account
    imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True, port="993")
    imapObj.login(sys.argv[1], sys.argv[2])
    imapObj.select_folder("INBOX", readonly=True)

    # Find mails only from last week
    lastWeek = datetime.date.today() - datetime.timedelta(days=7)
    messages = imapObj.search([u"SINCE", lastWeek])

    # Create dictionary to store data
    urls = {}

    # Iterate through every email and decode it
    for msgId in messages:
        rawMessage = imapObj.fetch(msgId, ["RFC822"])
        message = email.message_from_bytes(rawMessage[msgId][b"RFC822"])

        # Retrieve body of the email message
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'text/html':
                    body = part.get_payload(decode=True)

                    # Create HTML parser and retrieve sender name and email
                    soup = BeautifulSoup(body, "html.parser")
                    sender = message.get("From")

                    # Find and save links hidden inside paragraph
                    for p in soup.find_all("p"):
                        if "unsubscribe" in p.text:
                            anchor = p.find("a")
                            urls.setdefault(sender, anchor.get("href"))

                    # Find and save links inside anchors
                    for a in soup.find_all("a"):
                        if "unsubscribe" in a.text:
                            urls.setdefault(sender, a.get("href"))
                    break
    
    return urls


def openLinks(urls):
    '''
    Opens provided links reffering to unsubscribe pages in browser.
    '''

    for sender, url in urls.items():
        print(f"Opening unsubscribe page for {sender}...")
        webbrowser.open(url)


if __name__ == "__main__":
    openLinks(findUrls())

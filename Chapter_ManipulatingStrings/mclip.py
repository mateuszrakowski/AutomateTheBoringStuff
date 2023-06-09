#!/usr/bin/python
# mclip - A multi-clipboard program.


import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]     # first command line arg is the keyphrase


TEXT = {"agree": """Yes, I agree. That sounds fine to me.""",
        "busy": """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""}


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}.")
''' 
mcb.pyw - Saves and loads pieces of text to the clipboard
Usage:  mcb.py save <keyword> - Saves clipboard to keyword.
        mcb.py <keyword> - Loads keyword to clipboard.
        mcb.py list - Loads all keywords to clipboard.
'''


import shelve, pyperclip, sys


mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == "delete":
        for key in mcbShelf.keys():
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
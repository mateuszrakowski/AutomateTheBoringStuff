import re


example = "xDaletrudne2"


def strongPasswordDetector(txt):
    pswdCharacters = re.search(r"\w{8,}", txt)
    if pswdCharacters != None:
        pswdDigits = re.search(r"\d+", pswdCharacters.group())
        if pswdDigits != None:
            pswdUpper = re.search(r"[A-Z]+", pswdCharacters.group())
            if pswdUpper != None:
                return "Stronk"
    return "Not stronk"


print(strongPasswordDetector(example))
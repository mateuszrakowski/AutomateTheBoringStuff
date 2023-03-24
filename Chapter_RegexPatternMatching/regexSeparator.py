import re


example = "    Hello my name is Jeff."
result = []

def regSeparator(txt):
    split = re.split(r"\W+", txt, re.LOCALE)
    for element in split:
        if element != "":
            result.append(element)

    return result

print(regSeparator(example))
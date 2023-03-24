import re, sys


example = "Hey the meeting date is 01/02/2020, please don't forget!"

def isValidDate(txt):
    date = re.search(r"""   (0[1-9]|[1-2][0-9]|3[01])   # day
                            /                           # separator
                            (0[1-9]|1[0-2])             # month
                            /                           # separator
                            ([12]\d{3})                 # year
                            """, txt, re.VERBOSE)


    thirtyDays = ["04", "06", "09", "11"]

    if date != None:
        day, month, year = date.groups()
    else:
        sys.exit("Date not found.")

        
    if month in thirtyDays:
        if int(day) <= 30:
            return "Valid"
        return "Not valid"

    if month == "02":
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or \
        (int(year) % 400 == 0 and int(year) % 100 != 0):
            if int(day) <= 29:
                return "Valid"
        if int(day) <= 28:
            return "Valid"
        return "Not valid"
    
    return "Valid"


print(isValidDate(example))

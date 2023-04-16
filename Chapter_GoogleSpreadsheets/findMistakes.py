# findMistakes.py - Program that checks if total value in column is correct in provided spreadsheet

import ezsheets


# Load a Google Spreadsheet
try:
    ss = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
    sheet = ss[0]
except:
    sys.exit("Couldn't load spreadsheet.")

# Read every row starting from second
for rowNum in range(2, len(sheet.getRows()) + 2):
    # Check if row isn't empty
    if sheet.getRow(rowNum)[0] != "":
        # Check if total value is correct
        if int(sheet.getRow(rowNum)[0]) * int(sheet.getRow(rowNum)[1]) != int(sheet.getRow(rowNum)[2]):
            print(f"Invalid total value: {sheet.getRow(rowNum)[2]} in row number: {rowNum}.")

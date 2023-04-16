# downloadingFormsData.py - Get list of the email addresses from Google Spreadsheets collected by Google Forms.

import ezsheets, re, sys


if len(sys.argv) == 2:
    spreadsheetID = sys.argv[1]
else:
    sys.exit("Invalid number of arguments.")


# Load a Google Spreadsheet
try:
    ss = ezsheets.Spreadsheet(spreadsheetID)
except:
    sys.exit("Couldn't load spreadsheet.")

# Set first sheet of Spreadsheet
sheet = ss[0]

# Get column with emails
allColumns = sheet.getColumns()
allRows = sheet.getRows()

# Regex for finding email column
findEmail = re.compile(r"email|e-mail", re.IGNORECASE)

# Prepare variable to store email column number
emailColNum = None

# Assuming that first row is intended to be a label row
for row in allRows[0]:
    # Search for email column
    if findEmail.search(row):
        # Get email column number
        emailColNum = allRows[0].index(row)

# Check if email column exists
if emailColNum is not None:
    # Print emails list, skipping empty cells and label name
    print([email for email in allColumns[emailColNum][1:] if email != ""])
else:
    sys.exit("Couldn't find email column.")
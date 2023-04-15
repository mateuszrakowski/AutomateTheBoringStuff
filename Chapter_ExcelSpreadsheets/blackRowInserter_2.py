# blackRowInserter.py - In a given row number (first argument) insert provided number of blank rows (second argument). Second version.

from openpyxl.utils.exceptions import InvalidFileException
import sys, openpyxl


# Check CLI arguments
if len(sys.argv) == 4:
    rowNumber = int(sys.argv[1])
    blanksNumber = int(sys.argv[2])
else:
    sys.exit("Wrong number of arguments!")

# Open workbook from provided file name
try:
    wb = openpyxl.load_workbook(sys.argv[3])
except InvalidFileException:
    sys.exit("Invalid file format.")
except FileNotFoundError:
    sys.exit("File doesn't exist.")

# Copy spreadsheet
wbNew = wb
sheetNew = wbNew.active

# Insert rows
sheetNew.insert_rows(rowNumber, blanksNumber)

# Save to a new file
wbNew.save("New2_" + sys.argv[3])

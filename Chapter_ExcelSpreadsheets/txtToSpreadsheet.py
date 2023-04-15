# txtToSpreadsheet.py - Write contents of provided text files to Excel spreadsheet.

import openpyxl, sys


# Check CLI arguments
if len(sys.argv) < 2:
    sys.exit("Invalid number of arguments.")

# Create spreadsheet
wb = openpyxl.Workbook()
sheet = wb.active

# Create list to store files content
fileContents = []

# Read and open files one by one
for fileNum in range(1, len(sys.argv)):
    with open(sys.argv[fileNum], "r") as textFile:
        # Create nested lists - one list represents one file contents and one list element represents one line of txt file content
        fileContents.append([line.rstrip("\n") for line in textFile.readlines()])

# Write lines to cells - one column per file contents
# Starting loop from integer 1 decreases number of iterations by 1 - it's necessary to add one to maximum number of iterations
for colNum in range(1, len(fileContents) + 1):
    # List elements starts from index 0 - it's necessary to decrease colNum by 1
    for rowNum in range(1, len(fileContents[colNum - 1]) + 1):
        sheet.cell(row=rowNum, column=colNum).value = fileContents[colNum - 1][rowNum - 1]

wb.save("txtToSpreadsheet.xlsx")

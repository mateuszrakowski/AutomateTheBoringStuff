# spreadsheetsToOtherFormats.py - Converting Google Spreadsheet to other file format

import ezsheets, sys
import pyinputplus as pyip


# Check CLI arguments
if len(sys.argv) == 2:
    spreadsheetID = sys.argv[1]
else:
    sys.exit("Invalid number of arguments.")


# Load a Google Spreadsheet
try:
    ss = ezsheets.Spreadsheet(spreadsheetID)
except:
    sys.exit("Couldn't load spreadsheet.")

# Get information from user which format should be downloaded
print("Choose available format to download file.")
response = pyip.inputMenu(["Excel", "ODS", "CSV", "TSV", "PDF", "HTML"])

# Create complete method string
fileFormat = "downloadAs" + response

# Getattr makes it possible to call ss.DownloadAs method with 'response' variable
downloadFile = getattr(ss, fileFormat)

print(f"Downloading spreadsheet '{ss.title}' as {response} file...")
downloadFile()

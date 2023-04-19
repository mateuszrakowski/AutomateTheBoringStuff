# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF

import pypdf, os


# Get all the PDF filenames
pdfFiles = []

for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)

pdfWriter = pypdf.PdfWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, "rb")
    pdfReader = pypdf.PdfReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

# Save the resulting PDF to a file
pdfOutput = open("mergedFiles.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()

"""
pdfEncrypt.py - Find PDF files inside directory and subdirectories and encrypt files with provided password.
"""

import pypdf, os, sys


if len(sys.argv) == 2:
    pdfPassword = sys.argv[1]
else:
    sys.exit("Invalid number of arguments!")


def findFiles():
    """
    Find PDF files inside directory and subdirectories and return a list of file paths.
    """
    pdfFiles = []

    for directory, subdirectory, files in os.walk("."):
        for filename in files:
            if filename.endswith(".pdf"):
                pdfFiles.append(os.path.join(directory, filename))
    
    return pdfFiles


def createEncrypted(pdfList):
    """
    Create encrypted files and return list with filenames.
    """
    encryptedPdf = []
    
    for file in pdfList:
        reader = pypdf.PdfReader(file)
        writer = pypdf.PdfWriter()

        if reader.is_encrypted == False:
            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(pdfPassword)
            head, tail = os.path.split(file)

            # Save new encrypted file to the same directory path as original file
            with open(os.path.join(head, f"_encrypted_{tail}"), "wb") as f:
                writer.write(f)
                encryptedPdf.append(os.path.join(head, f"_encrypted_{tail}"))

    return encryptedPdf


def checkEncrypt(encryptedList, pdfList):
    """
    Check if files have been correctly encrypted and delete original files.
    """
    for encrypted in encryptedList:
        enc = pypdf.PdfReader(encrypted)

        # Split encrypted file path and create original file path
        head, tail = os.path.split(encrypted)
        originalFilename = os.path.join(head, tail.strip("_encrypted_"))

        if enc.is_encrypted:
            if enc.decrypt(pdfPassword):
                if originalFilename in pdfList:
                    os.remove(originalFilename)


if __name__ == "__main__":
    encryptedPdfs = createEncrypted(findFiles())
    checkEncrypt(encryptedPdfs, findFiles())

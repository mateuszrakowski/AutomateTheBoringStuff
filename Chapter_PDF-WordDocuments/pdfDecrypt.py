"""
Decrypts all PDF files in the current directory and its subdirectories using a password provided by the user.

Usage:
python decrypt.py <password>

Arguments:
password (str): The password to decrypt the PDF files.

Returns:
list: A list of decrypted PDF files.
"""

import pypdf, argparse, sys
from pathlib import Path


def checkPassword():
    """
    Prompts the user to enter a password to decrypt PDF files.

    Returns:
    str: The password entered by the user.
    """
    parser = argparse.ArgumentParser(description="Decrypt PDF files in a directory.")
    parser.add_argument("password", help="Password to decrypt the PDF files.")
    args = parser.parse_args()
    return args.password


def findFiles():
    """
    Finds all PDF files in the current directory and its subdirectories.

    Returns:
    list: A list of PDF files.
    """
    listOfPdf = []
    for path in Path(".").rglob("*.pdf"):
        listOfPdf.append(str(path))
    return listOfPdf


def decryptFiles(fileList):
    """
    Decrypts a list of PDF files using the password provided by the user.

    Args:
    fileList (list): A list of PDF files to be decrypted.

    Returns:
    list: A list of decrypted PDF files.
    """
    decryptedList = []
        
    for pdfFile in fileList:
        reader = pypdf.PdfReader(pdfFile)
        writer = pypdf.PdfWriter()

        if reader.is_encrypted:
            try:
                reader.decrypt(checkPassword())
                for page in reader.pages:
                    writer.add_page(page)
                
                pdfPath = Path(pdfFile)
                with open(Path(pdfPath.parent / f"_decrypted_{pdfPath.name}"), "wb") as f:
                    writer.write(f)
                    decryptedList.append(f"_decrypted_{pdfPath.name}")
            except:
                print(f"Wrong password to {pdfFile}!")
    
    return decryptedList


if __name__ == "__main__":
    decryptedFiles = decryptFiles(findFiles())
    print(decryptedFiles)

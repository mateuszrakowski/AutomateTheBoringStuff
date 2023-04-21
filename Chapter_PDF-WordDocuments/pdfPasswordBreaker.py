"""
Breaks the encrypted PDF file with brute-force password attack using English dictionary.

Usage:
python pdfPasswordBreaker.py <txt filename>

Returns:
str: Valid password to PDF file.
"""

import pypdf, argparse
from pathlib import Path


def checkExtension(filename):
    """
    Check if provided filename is .pdf file.

    Returns:
    str: The filename entered by user.
    """
    if not filename.endswith(".pdf"):
        raise argparse.ArgumentTypeError("File must have .pdf extension.")
    return filename


def checkPdf():
    """
    Prompts the user to enter a filename or path.

    Returns:
    str: The filename entered by user.
    """
    parser = argparse.ArgumentParser(description="Breaks the encrypted PDF file with brute-force password attack using English dictionary.")
    parser.add_argument("filename", help="Name or path of PDF file to decrypt.", type=checkExtension)
    args = parser.parse_args()
    return args.filename


def findPassword(pdfFile, dictionary):
    """
    Finds matching password to encrypted PDF file using English dictionary.

    Returns:
    str: Matching password.
    """
    reader = pypdf.PdfReader(pdfFile)
        
    if reader.is_encrypted:
        try:
            with open(dictionary, "r") as englishDict:
                for word in englishDict:
                    matchPassword = word.strip()
                    if reader.decrypt(matchPassword):
                        return f"Matching password found: {matchPassword}."
                    if reader.decrypt(matchPassword.lower()):
                        return f"Matching password found: {matchPassword.lower()}."
                    print(matchPassword)
        except:
            return "Couldn't find dictionary file!"
    else:
        return "File is not encrypted!"
    return "Match not found!"


if __name__ == "__main__":
    print(findPassword(checkPdf(), "dictionary.txt"))


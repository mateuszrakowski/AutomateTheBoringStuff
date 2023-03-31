'''
regexFileSearch.py - Searches through all text files inside directory for given regex pattern.
Prints found matches in a list as a result.
'''

from pathlib import Path
import re


# Get regex from user
reUser = input("Write regex:\n")
matches = []

# Find txt files inside directory
p = Path.cwd()
txtFiles = list(p.glob('*.txt'))

# Open files in directory
for txtFile in txtFiles:
    with open(txtFile) as file:
        # Store matches
        matches.append(re.findall(f"{reUser}", file.read()))

# Print found matches
print(matches)

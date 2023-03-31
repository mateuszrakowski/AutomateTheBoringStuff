'''
madLibs.py - Creates the updated text file with given words from the user.
File to be read must have prepared words to replace.
'''


import re


# Path to file
file = "panda.txt"

# Open and read file
with open(file) as textFile:
    words = textFile.read().split()
    # Iterate through words
    for i in range(len(words)):
        # Look for pattern
        if re.search(r"ADVERB|VERB|ADJECTIVE|NOUN", words[i]):
            # If last word of sentence remove & add dot
            if words[i][-1] == ".":
                words[i] = words[i].rstrip(".")
                ask = input(f"Enter an {words[i].lower()}:\n")
                words[i] = ask + "."
            # Update word to user input
            else:
                words[i] = input(f"Enter an {words[i].lower()}:\n")

# Create and save new file with previously created list
with open(f"madLibs_{file}", "w") as newFile:
    newFile.write(" ".join(words))

# Print out the result
print(" ".join(words) + "\n")

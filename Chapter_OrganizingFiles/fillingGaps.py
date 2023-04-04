''' fillingGaps.py - Searching for files with given prefix which has "gaps" in numerical order.
    fillGaps(directory, prefix) - Changes found "gaps" to correct numerical order.
    insertGaps(directory, prefix, index) - Creates "gap" in numerical order in given index position.
    Files has to have extension. Index argument represents number of filename.
'''

import os, re, shutil


def findFiles(directory, prefix):
    # Get absolute path of directory
    directory = os.path.abspath(directory)
    # Create list to store filenames
    filesList = []

    # Search for files inside directory
    for file in os.listdir(directory):
        if file.startswith(prefix):
            # Store filenames in created list
            filesList.append(file)
    
    # Sort list in ascending order
    filesList.sort()
    return filesList


def fillGaps(directory, prefix):
    filesList = findFiles(directory, prefix)

    for i in range(len(filesList) - 1):
        # Find & extract numerical order from filenames
        numericalOrder = re.compile(r"\d+")
        firstNumber = numericalOrder.search(filesList[i]).group(0)
        nextNumber = numericalOrder.search(filesList[i+1]).group(0)
        
        # Compare numbers
        if (int(nextNumber) - int(firstNumber)) > 1:
            # Extract leading zero if exist
            zero = re.search(r"^0+", nextNumber)
            # Save it to variable
            if zero is not None:
                leadZero = zero.group(0)
            
            # Save file extension to variable
            suffix = filesList[i+1].lstrip(prefix + nextNumber)
            # Change filename inside list with correct numerical order
            oldFilename = filesList[i+1]
            filesList[i+1] = f"{prefix}{leadZero}{int(firstNumber) + 1}{suffix}"
    
            # Create path with old filename and path with new filename
            newFilePath = os.path.abspath(os.path.join(directory, filesList[i+1]))
            oldFilePath = os.path.abspath(os.path.join(directory, oldFilename))

            # Change names and print progress to user
            print(f"Changing name of {oldFilename} to {filesList[i+1]}...")
            shutil.move(oldFilePath, newFilePath)


def insertGaps(directory, prefix, index):
    filesList = findFiles(directory, prefix)

    # Find largest number in numerical order
    numericalOrder = re.compile(r"\d+")
    largestNumber = int(numericalOrder.search(filesList[-1]).group(0))

    for i in range(len(filesList)):
        # Locate last filename in list to prevent overwriting files by changing files starting from end of the list
        lastFile = len(filesList) - i - 1

        # Find & extract numerical order from filenames
        firstNumber = numericalOrder.search(filesList[lastFile]).group(0)
        
        # Rename files from the highest filename number up to and including the specified index number
        if i <= (largestNumber - int(index)):
            # Extract leading zero if exist
            zero = re.search(r"^0+", firstNumber)
            # Save it to variable
            if zero is not None:
                leadZero = zero.group(0)
            
            # Save file extension to variable
            suffix = filesList[lastFile].lstrip(prefix + firstNumber)
            # Change filename inside list with correct numerical order
            oldFilename = filesList[lastFile]
            filesList[lastFile] = f"{prefix}{leadZero}{int(firstNumber) + 1}{suffix}"

            # Create path with old filename and path with new filename
            newFilePath = os.path.abspath(os.path.join(directory, filesList[lastFile]))
            oldFilePath = os.path.abspath(os.path.join(directory, oldFilename))

            # Change names and print progress to user
            print(f"Changing name of {oldFilename} to {filesList[lastFile]}...")
            shutil.move(oldFilePath, newFilePath)
        else:
            break

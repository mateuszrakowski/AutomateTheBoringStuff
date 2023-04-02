# selectiveCopy.py - Copy files with specified extension to new directory

import shutil, os


def selectiveCopy(folder, extension):
    # Create absolute path of the folder
    folder = os.path.abspath(folder)
    newDirectory = os.path.join(folder, "extensionCopies")

    # Create directory to save found files
    if not os.path.exists(newDirectory):
        os.mkdir(newDirectory)

    # Look for specified file extension inside folder
    for foldername, subfolders, filenames in os.walk(folder):
        if foldername == newDirectory:
            continue

        print(f"Looking for {extension} files inside {foldername}...")

        # Copy file to new directory
        for filename in filenames:
            if filename.endswith(extension):
                print(f"Copying {filename} to new directory...")
                shutil.copy(os.path.join(foldername, filename), newDirectory)

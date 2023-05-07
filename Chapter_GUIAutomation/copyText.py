'''
Opens file from provided path and copies whole text content to clipboard and saves as variable.

Usage:
python3 copyText.py <path to file>
'''

import pyautogui, time, os, pyperclip, sys


# Open file
os.system(f"open {sys.argv[1]}")
time.sleep(2)

# Select whole content and store in clipboard
with pyautogui.hold(['command']):
    time.sleep(1)
    pyautogui.press('a')
    time.sleep(1)
    pyautogui.press('c')
    time.sleep(1)

# Copy content to variable
copiedText = pyperclip.paste()

# Print copied text content
print(copiedText)

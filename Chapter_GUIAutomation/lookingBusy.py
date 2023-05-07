'''
Simulates mouse movement to prevent other applications setting status as away from keyboard.

Usage:
python3 lookingBusy.py
'''

import pyautogui, time


time.sleep(5)
print("Press CTRL+C to interrupt.")

while True:
    pyautogui.moveTo(500, 600, 2)
    pyautogui.moveTo(600, 600, 2)
    pyautogui.moveTo(600, 700, 2)
    pyautogui.moveTo(500 ,700, 2)
    time.sleep(5)

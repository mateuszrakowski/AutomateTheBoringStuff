"""
A simple countdown script with sound alert.

Usage:
python countdown.py
"""

import time, subprocess


timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end="")
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file
subprocess.Popen(["open", "alarm.wav"])

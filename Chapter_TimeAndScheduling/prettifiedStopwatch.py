'''
A simple stopwatch program with nicely displayed results.

Usage:
Program instructions are displayed after startup.
'''

import time, pyperclip


# Display the program's instructions
print("Press ENTER to begin. Afterward, press ENTER to 'click' the stopwatch. Press CTRL-C to quit.")

# Press enter to begin
input()
print("Started")

textToCopy = ""
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        outputText = f"Lap # {lapNum}: {str(totalTime).rjust(7)} ({str(lapTime).rjust(7)})"
        textToCopy += outputText + "\n"
        print(outputText, end="")
        lapNum += 1
        lastTime = time.time() # Reset the last lap time
except KeyboardInterrupt:
    # Handle the CTRL-C exception
    print("\nDone. Results have been copied to the clipboard.")

pyperclip.copy(textToCopy)

'''
A simple stopwatch program.

Usage:
Program instructions are displayed after startup.
'''

import time


# Display the program's instructions
print("Press ENTER to begin. Afterward, press ENTER to 'click' the stopwatch. Press CTRL-C to quit.")

# Press enter to begin
input()
print("Started")

startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {totalTime} ({lapTime})", end="")
        lapNum += 1
        lastTime = time.time() # Reset the last lap time
except KeyboardInterrupt:
    # Handle the CTRL-C exception
    print("\nDone.")

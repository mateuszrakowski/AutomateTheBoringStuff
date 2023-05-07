"""
Automatically fills the Google Form.

Usage:
python3 formFiller.py
"""

import pyautogui, time


formData = [
    {
        "name": "Alice",
        "fear": "eavesdroppers",
        "source": "wand",
        "robocop": 4,
        "comments": "Tell Bob I said hi.",
    },
    {
        "name": "Bob",
        "fear": "bees",
        "source": "amulet",
        "robocop": 4,
        "comments": "n/a",
    },
    {
        "name": "Carol",
        "fear": "puppets",
        "source": "crystal ball",
        "robocop": 1,
        "comments": "Please take the puppets out of the break room.",
    },
    {
        "name": "Alex Murphy",
        "fear": "ED-209",
        "source": "money",
        "robocop": 5,
        "comments": "Protect the innocent. Serve the public trust. Uphold the law.",
    },
]


pyautogui.PAUSE = 0.5
print("Ensure that the browser window is active and the form is loaded!")

for person in formData:
    # Give the user a chance to kill the script
    print(">>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<")
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    pyautogui.write(["\t", "\t", "\t"])

    # Fill out the Name field
    pyautogui.write(person["name"] + "\t")

    # Fill out the Greates Fear(s) field
    pyautogui.write(person["fear"] + "\t")

    # Fill out the Source of Wizard Powers field
    if person["source"] == "wand":
        pyautogui.write(["down"], 0.5)
        pyautogui.press("enter")
    elif person["source"] == "amulet":
        pyautogui.write(["down", "down"], 0.5)
        pyautogui.press("enter")
    elif person["source"] == "crystal ball":
        pyautogui.write(["down", "down", "down"], 0.5)
        pyautogui.press("enter")
    elif person["source"] == "money":
        pyautogui.write(["down", "down", "down", "down"], 0.5)
        pyautogui.press("enter")
    pyautogui.write("\t")

    # Fill out the RoboCop field
    if person["robocop"] == 1:
        pyautogui.write([" ", "\t", "\t"], 0.5)
    elif person["robocop"] == 2:
        pyautogui.write(["right", "\t", "\t"])
    elif person["robocop"] == 3:
        pyautogui.write(["right", "right", "\t", "\t"])
    elif person["robocop"] == 4:
        pyautogui.write(["right", "right", "right", "\t", "\t"])
    elif person["robocop"] == 5:
        pyautogui.write(["right", "right", "right", "right", "\t", "\t"])

    # Fill out the Additional Comments field
    # pyautogui.write("Tell Bob I said hi.")

    # "Click" submit button by pressing Enter
    pyautogui.write("\t")
    time.sleep(0.5)
    pyautogui.press("enter")

    # Wait until form page has loaded
    print("Submitted form")
    time.sleep(5)

    # Click the Submit another response link
    pyautogui.click(512, 265)

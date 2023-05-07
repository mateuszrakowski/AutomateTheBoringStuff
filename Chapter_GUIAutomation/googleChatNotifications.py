"""
Opens Google Chat in browser and sends notifications messages to provided usernames from friendlist.

Usage:
python3 googleChatNotifications.py 
"""

import webbrowser, pyautogui, time


notifications = {"username": "username", "message": "Hey its me!"}

# Open browser and wait for load page
webbrowser.open("https://mail.google.com/chat")
time.sleep(5)

# Select proper user from friendlist and open chat
pyautogui.write(["\t", "\t"], 0.5)
pyautogui.write(notifications["username"], 0.5)
pyautogui.write(["down"], 0.5)
pyautogui.press("enter")

# Focus action on chat and write message
time.sleep(2)
pyautogui.click(598, 837)
pyautogui.write(notifications["message"], 0.5)
pyautogui.press("enter")

# Close browser
print("Message sent.")

"""
Randomly assigns chores to people and sends them emails with instructions.

Usage:
python3 choreEmailAssignment.py <email password>
"""

import random, smtplib, pickle, sys


# Store chores and emails addresses
chores = ["dishes", "bathroom", "vacuum", "walk dog"]
emails = ["examplemail1@gmail.com", "examplemail2@gmail.com", "examplemail3@gmail.com", "examplemail4@gmail.com"]


def setChores():
    """
    Build dictionary with chores assignments.

    Returns:
    dict: Dictionary with assigned chores to email addresses.
    """
    assignments = {}
    filename = "lastChoresAssignments.pk"

    # If previously chores have beed assigned, load data to prevent setting same chore to same email address
    try:
        with open(filename, "rb") as fi:
            lastAssignment = pickle.load(fi)
    # If program is run for first time or no data is present
    except:
        lastAssignment = {}

    for email in emails:
        # Pick random chore
        randomChore = random.choice(chores)

        # Set and save assignments
        if lastAssignment == {}:
            assignments[email] = randomChore
            chores.remove(randomChore)
        else:
            # Make sure to assignment different chore than last time
            while lastAssignment[email] == randomChore:
                randomChore = random.choice(chores)
            assignments[email] = randomChore
            chores.remove(randomChore)

    # Save assignments to file
    if lastAssignment == {}:
        lastAssignment = assignments

    with open(filename, "wb") as fi:
        pickle.dump(lastAssignment, fi)

    return assignments


def sendEmails(assignments):
    """
    Sends emails with assigned chores to every provided email address.

    Returns:
    str: Information about email status.
    """

    # Create smtp object and log in to email account
    smtpObj = smtplib.SMTP("smtp.server.com", "587")
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("youremail@gmail.com", sys.argv[1])

    # Send out reminder emails
    for email, chore in assignments.items():
        body = f"Subject: Your today chore: {chore}.\nHey,\nI kindly remaind You about Your today chore, which is {chore}. Thanks in advance :)"
        print(f"Sending email to {email}...")
        sendmailStatus = smtpObj.sendmail("youremail@gmail.com", email, body)

        if sendmailStatus != {}:
            print(f"There was a problem sending email to {email}: {sendmailStatus}.")
    smtpObj.quit()


if __name__ == "__main__":
    sendEmails(setChores())

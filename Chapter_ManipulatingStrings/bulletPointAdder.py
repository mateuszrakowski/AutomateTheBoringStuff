import pyperclip


def main():
    bulletPoints()


def bulletPoints():
    text = pyperclip.paste()

    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)):    # loop through all indexes for "lines" list
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list
    
    text = '\n'.join(lines)
    pyperclip.copy(text)

if __name__ == "__main__":
    main()
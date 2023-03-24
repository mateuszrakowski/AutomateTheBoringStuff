# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

def main():
    spam = input("Pick a number from 1 to 3: ")

    print(greetings(spam))


def greetings(string):
    if string == "1":
        return "Hello"
    elif string == "2":
        return "Howdy"
    return "Greetings!"


if __name__ == "__main__":
    main()

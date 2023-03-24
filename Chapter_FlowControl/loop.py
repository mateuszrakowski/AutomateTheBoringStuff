# Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


def main():
    for_loop()
    print("")
    while_loop()


def for_loop():
    for i in range(10):
        print(i+1)


def while_loop():
    i = 0

    while i < 10:
        i += 1
        print(i)


if __name__ == "__main__":
    main()

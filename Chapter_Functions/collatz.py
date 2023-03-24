import sys


def main():
    number = input("Enter number:\n")
    collatz(number)


def collatz(i):
    try:
        num = int(i)

        while num != 1:
            if num % 2 == 0:
                num = num // 2
                print(num)
            elif num % 2 == 1:
                num = 3 * num + 1
                print(num)
        return num

    except ValueError:
        sys.exit("Please enter an integer")


if __name__ == "__main__":
    main()

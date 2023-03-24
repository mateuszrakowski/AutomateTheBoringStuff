import random

def main():
    print(flip())


def flip():
    numberOfStreaks = 0
    results = []
    streaks = 0
    containsStreak = False

    for experimentNumber in range(10000):

        for i in range(100):
            results.append(random.randint(0, 1))
            
        for i in range(len(results)):
            if i == 0:
                pass
            elif results[i] == results[i-1]:
                streaks += 1
            else:
                streaks = 0
        
            if streaks == 6:
                containsStreak = True
        if containsStreak:
            numberOfStreaks += 1
        
        results = []
        containsStreak = False

    return f"Chance of streak: {numberOfStreaks / 100}%"


if __name__ == "__main__":
    main()
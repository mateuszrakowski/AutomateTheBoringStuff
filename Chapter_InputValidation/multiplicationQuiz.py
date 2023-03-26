import pyinputplus as pyip
import random, time


def quiz():
    numberOfQuestions = 10
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        # Pick two random numbers
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = f"#{questionNumber + 1}: {num1} * {num2} = "

        try:
            # Right answers are handled by AllowRegexes
            # Wrong answers are handled by BlockRegexes
            pyip.inputStr(prompt, allowRegexes=[f"^{num1 * num2}$"], blockRegexes=[(".*", "Incorrect!")], timeout=8, limit=3)
        except pyip.TimeoutException:
            print("Out of time!")
        except pyip.RetryLimitException:
            print("Out of tries!")
        else:
            # This block runs if no exceptions were raised in the try block
            print("Correct!")
            correctAnswers += 1
        
        time.sleep(1) # Brief pause to let user see the result
    print(f"Score: {correctAnswers} / {numberOfQuestions}")


quiz()
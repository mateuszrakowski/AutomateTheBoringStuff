import random, time


def quiz():
    numberOfQuestions = 10
    correctAnswer = 0

    for questionNumber in range(numberOfQuestions):
        # Pick two random numbers
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        # Quiz mathematic question
        prompt = f"#{questionNumber + 1}: {num1} * {num2} = "

        # Save time to variable every question asked
        timeout = time.perf_counter()

        for i in range(4):
            # Handles number of tries with limit to 3
            if i == 3:
                print("Out of tries!")
                break

            try:
                answer = int(input(prompt))

                # Right answer
                if answer == num1 * num2:
                    correctAnswer += 1
                    print("Correct!")
                    break
                # Wrong answer
                print("Incorrect!")

            # Wrong input, eg. string
            except ValueError:
                print("Incorrect!")

            # Check how many time passed, break if more than 8 seconds
            if (time.perf_counter() - timeout) > 8:
                print("Out of time!")
                break

        time.sleep(1)
    print(f"Score: {correctAnswer} / {numberOfQuestions}")


quiz()

import random, time


def quiz():
    numberOfQuestions = 10
    correctAnswer = 0

    for questionNumber in range(numberOfQuestions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = f"#{questionNumber + 1}: {num1} * {num2} = "

        for i in range(3):
            try:
                answer = int(input(prompt))
    
                if answer == num1 * num2:
                    correctAnswer += 1
                    print("Correct!")
                    break
                print("Incorrect!")
            
            except ValueError:
                print("Incorrect!")
        
        print("Out of time!")
    print("Out of tries!")  


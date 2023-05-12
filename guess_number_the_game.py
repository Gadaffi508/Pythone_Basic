from random import randint

Easy_Level_Turns = 10
Hard_Level_Turns = 5

def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : \n")
    if level == "easy":
        return Easy_Level_Turns
    else:
        return Hard_Level_Turns

def game():
    print("Welcome to the number Guessing Game!")
    print("I'm  thinking of a number between 1 and 100.")

    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns=set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a Guess : \n"))
        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
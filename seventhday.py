import random

stages = "Öldü","Son bacak","Son iki ayak","Son kol","Son İki kol","Kafa","İp"
lives = 6

world_list = ["dog","puma","wolf","crocodile"]

#T0D0-1 Randomly choose a word from the world_list and assign it to a variable called chosen_word.
chosen_word = random.choice(world_list)

#Testing Code
print(f"Be quited {chosen_word}")

#T0D0-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
world_length = len(chosen_word)
for _ in range(world_length):
    display += "_"
print(display)

end_of_games = False

while not end_of_games:
    guess = input("Guess a letter : ").lower() 
    #T0D0-3 check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(world_length):
        letter = chosen_word[position]
        #print(f"Current position: {position} \n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_games = True
            print("You Lose")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_games = True
        print("You Win")
        
    print(stages[lives])
import random
num = random.randint(1, 20)
guess = 0

while True:   
    guess = (input("Guess a number between 1 and 20: "))

    if guess == "x":
        print("You quit the game")
        break

    elif int(guess) == num:
        print("You guessed the correct number!")
        break
    
    elif int(guess) > num:
        print("Your guess is higher than the number")

    elif int(guess) < num:
        print("Your guess is lower than the number")
import random
num = random.randint(1, 20)
guess = 0
debug = False
move = False
margin = [-2, -1, 0, 1, 2]

while True:
    if debug:
        print("Debug mode: The number is ", num)

    if move:
        num += random.choice(margin)
        num = max(1, min(num, 20))

    guess = (input("Guess a number between 1 and 20: "))

    if guess == "x":
        print("You quit the game")
        break

    elif guess == "s":
        print("The number is ", num," you cheater")
        break

    elif guess == "d":
        debug = not debug
        if debug:
            print("Debug mode: ON")
        else:
            print("Debug mode: OFF")
    
    elif guess == "m":
        move = not move
        if move:
            print("Move mode: ON")
        else:
            print("Move mode: OFF")

    elif guess == "n":
        num = random.randint(1, 20)
        print("New game!")
        continue

    elif int(guess) == num:
        print("You guessed the correct number!")
        break
    
    elif int(guess) > num:
        print("Your guess is higher than the number")

    elif int(guess) < num:
        print("Your guess is lower than the number")
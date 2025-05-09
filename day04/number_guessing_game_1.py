import random
num = random.randint(1, 20)
guess = 0

while num != guess:   
    guess = int(input("Guess a number between 1 and 20: "))

    if guess > num:
        print("Your guess is higher than the number")

    elif guess < num:
        print("Your guess is lower than the number")

print("You guessed the correct number!")
import random

num = random.randint(1, 20)
guess = input("Guess a number between 1 and 20: ")

if guess == num:
    print("You guessed the correct number!")

elif guess < num:
    print("Your guess is lower than the number")

else:
    print("Your guess is higher than the number")
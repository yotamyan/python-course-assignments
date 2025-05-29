import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    colors = [line.strip().lower() for line in file if line.strip()]

user_input = input("Enter a color: ").strip().lower()

if user_input in colors:
        print(f"Color '{user_input}' is in the list!")
else:
        print(f"Color '{user_input}' is NOT in the list.")
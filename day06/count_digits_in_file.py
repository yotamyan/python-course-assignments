import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    content = file.read()

count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for char in content:
    if char.isdigit():
        count[int(char)] += 1

with open("report.txt", 'w') as file:
    for digit, frequency in count.items():
        file.write(f"{digit} {frequency}\n")
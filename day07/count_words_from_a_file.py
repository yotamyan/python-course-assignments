import sys

filename = sys.argv[1]
count = {}

with open(filename, 'r') as file:
    words = [word.strip().lower() for line in file for word in line.split() if word.strip()]

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for i in count:
    print(f"{i} {count[i]}")
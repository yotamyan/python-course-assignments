numbers = [1203, 1256, 312456, 98]

counter = {i: 0 for i in range(10)}
for number in numbers:
    for digit in str(number):
        counter[int(digit)] += 1

for i in counter:
    print(i, counter[i])
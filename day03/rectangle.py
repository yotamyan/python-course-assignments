import sys

height = float(sys.argv[1])
width = float(sys.argv[2])

P = 2 * height + 2 * width
A = height * width

print(f"The perimeter of your rectangle is: {P}")
print(f"The area of your rectangle is: {A}")
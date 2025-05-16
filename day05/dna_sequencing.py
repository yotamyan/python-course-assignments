import sys

sequence = sys.argv[1]

parts = sequence.split("X")
cleaned = [p for p in parts if p]
sorted_parts = sorted(cleaned, key=len, reverse=True)

print (sorted_parts)
import sys
import re

sequence = input("Enter a DNA sequence: ")

parts = re.findall(r'[ACTG]+', sequence)
sorted_parts = sorted(parts, key=len, reverse=True)

print (sorted_parts)
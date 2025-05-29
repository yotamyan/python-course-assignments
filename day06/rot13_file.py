import sys
import codecs

filename = sys.argv[1]

with open(filename, 'r') as file:
    content = file.read()

rot13_content = codecs.encode(content, 'rot_13')

with open(filename, 'w') as file:
    file.write(rot13_content)

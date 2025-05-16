celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

counter = {}

for word in celestial_objects:
    counter[word] = 0

for word in celestial_objects:
    counter[word] += 1

for i in counter:
    print(i, counter[i])
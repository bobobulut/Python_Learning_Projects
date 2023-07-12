abc = "With three words"
stuff = abc.split()

print(abc)
print(stuff)
print(len(stuff))
print(stuff[1])

print("\n")

for i in stuff:
    print(i)

print("--------\n")

line = "A lot               of spaces"
etc = line.split()
print(etc)

print("\n")
...
line = "First;second;third"

thing = line.split()
print(thing)
print(len(thing))

thing = line.split(";")
print(thing)
print(len(thing))
s="Deneme Metni"
print(len(s))
print(s[:2])
print(s[8:])
print(s[4:7])
print(s[7:20])

print()

lower_s = s.lower()
print(lower_s)
print("BU DA BİR DENEME".lower())

print()
print(type(s))
print(dir(s))

print()

word = "bananana"
i = word.find("na")
print(i)

line="Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("P"))
print(line.startswith("p"))

stuff = "Hello\nWorld"
print(stuff)
print(len(stuff))
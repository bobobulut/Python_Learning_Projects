print("Word Counter")
counts = dict()
print("Enter a line of text")
line = input("> ")

words = line.split()

print("Words:", words)

print("Counting...")
for word in words:
    counts[word] = counts.get(word,0) + 1
print("Counts", counts)

print("--------\n")

#Yol 1
counts = {"Chuck": 1, "Fred": 42, "Jan": 100}
for key in counts:
    print(key, counts[key])

print()

#Yol2
for aaa,bbb in counts.items():
    print(aaa,bbb)

print()

print("List:", list(counts))
print("Keys:", counts.keys())
print("Values", counts.values())
print("Items", counts.items())

print("--------\n")

#Bir belge içerisindeki en çok tekrar eden kelimeyi verir
#/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf
name = input("Enter a file name: ")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1 

print()

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

print("--------\n")

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
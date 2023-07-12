import urllib.request, urllib.parse, urllib.error
# import urllib

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

print("-------\n")

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

print("-------\n")

fhand = urllib.request.urlopen("http://dr-chuck.com/page1.htm")
for line in fhand:
    print(line.decode().strip())


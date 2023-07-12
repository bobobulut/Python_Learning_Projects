import re
#tüm kaynaklar 
#https://docs.python.org/3/library/re.html

hand = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")

#Yol 1
for line in hand:
    line = line.rstrip()
    if line.find("From") >= 0:
        print(line)

#Yol 2
for line in hand:
    line = line.rstrip()
    if line.startswith("From"):
        print(line)

#Yol 3
for line in hand:
    line = line.rstrip()
    if re.search("From", line):
        print(line)

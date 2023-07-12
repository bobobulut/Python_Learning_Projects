file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
count = 0 
for i in file_name:
    count = count + 1 
print("Line count is ", count)

print("-------\n")

file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
inp = file_name.read()
print(len(inp))
print(inp[:1000])

print("-------\n")

file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
for k in file_name:
    if k.startswith("From"):
        print(k)

print("-------\n")

file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
for line in file_name:
    line = line.rstrip()
    if line.startswith("From"):
       print(line)

print("-------\n")

file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
for line in file_name:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    print(line)

print("-------\n")

file_name = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
for line in file_name:
    line = line.rstrip()
    if not "From" in line:
        continue
    print(line)

print("-------\n")

#/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf
file_name = input("Enter the file name: ")
try:
    open_file = open(file_name)
except:
    print("File cannot be opened: ", file_name)
    quit()
count=0
for line in open_file:
    if line.startswith("From"):
        count += 1 
print("There wew", count, "subject lines in", file_name,"\n")

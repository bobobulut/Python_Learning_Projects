#örnek 1

x = "Hello"

try:
    i = int(x)
except:
    i=-1

print("First", i)

x="123"
try:
    i = int(x)
except:
    i = -1
print("Second", i)


print()
print()
print()
#örnek 2

temp = input("Enter a value for calcuation > ")
cel = 0
try:
    fahr = float(temp)
except:
    fahr = float(input("Sorrry, Enter fahr value > "))
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)


print()
print()
print()
#örnek 3

rawst = input ("Enter a number > ")
try:
    i = int(rawst)
except:
    i = -1

if i > 0:
    print("Nice Work!")
else:
    print("Not a number")
fruit = input("Enter a fruit name: ")
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index=index+1

print()

for letter in fruit:
    print(letter)

print()

count=0
for letter in fruit:
    if letter =="a":
        count=count+1
print(count)

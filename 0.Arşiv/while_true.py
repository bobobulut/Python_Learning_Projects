#example 1 

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")

print()
print()
print()
#example 2

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss" or lyrics == "Miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")

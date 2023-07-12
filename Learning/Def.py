#örnek 1 

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "Bora" and password == "bora1234":
      print("Welcome Bora!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("REPLIT LOGIN SYSTEM")
login()

print()
print()
#örnek 2

def greet(lang):
  if lang == "tr":
    print("Merhaba")
  elif lang == "fr":
    print("Bonjour!")
  elif lang == "eng":
    print("Hello!")
  else:
    print("I dont't know that language...")

def greet_all(lang):
  if lang == "tr":
    return "Merhaba"
  elif lang == "fr":
    return "Bonjour"
  elif lang == "eng":
    return "Hello!"
  else:
    return "I dont't know that language..."
  
print (greet_all("tr"), "Bora")
print(greet_all("fr"), "Sude")

print()
print()
#örnek 2

def addtwo(a,b):
  added = a + b
  return added
x = addtwo(3,5)
print(x)

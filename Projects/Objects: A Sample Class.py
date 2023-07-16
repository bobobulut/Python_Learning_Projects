class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()

an.party()  # = Party.Animal.party(an)
an.party()
an.party()

print("-------\n")

print("Type: ", type(an))
print("Dir: ", dir(an)) # you will see the functions that you added = ... 'party', 'x']

print("-------\n")

x = list()
type(x)
print(dir(x))

print("-------\n")

y = "String"
print(dir(y))

print("-------\n")


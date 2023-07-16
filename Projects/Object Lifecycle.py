class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam): # Will automaticly avtivate before object is created and destroyed.
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)
    def __del__(self): # Will automaticly avtivate before object is created and destroyed.
        print(self.name, "is destructed. Last count :", self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()
q.party()
m.party()
m = "Test"
print("m is ", m, "now.")
q.party()
q = "Test"
print("q is ", q, "now.")
x = ("Gleen", "Sally", "Josheph")
print(x[2])
#tuple dediğimiz parantezlerde düzenleme ve diğer fonskiyonları kullanamıyoruz
print()
i = list()
t = tuple()
print("List Fonksiyonları: ", dir(i))
print("Tuple Fonskiyonları: ", dir(t))

print("--------\n")

y = (1,9,2)
print(y)
print(max(y))

print()

for iter in y:
    print(iter)

print("--------\n")

(x,y) = (4, "fred")
print(y)
print()
(a,b) = (99,98)
print(a)

print("--------\n")

d = dict()
d["csev"]=2
d["cwen"]=4
for k,v in d.items():
    print(k,v)
print()
tups = d.items()
print(tups)
for i in [5,4,3,2,1]:
    print(i)
print("Kalkış!!")

print("-------\n")

isimler = ["Ali", "Veli", "Ahmet", "Mehmet"]
for isim in isimler:
    print("Merhaba", isim)
print("\nHerkes tamam.\n")
print(isimler[2], "\n")

for i in range(len(isimler)):
    isim_2= isimler[i]
    print("Bu kişinin ismi", isim_2)

print("-------\n")

büyük = "DENEMEBirİki"
küçük = büyük.lower()
print(büyük)
print(küçük)
print(len(küçük))

print("-------\n")

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 100
print(lotto)
print(len(lotto))
print(range(len(lotto)))

print("-------\n")

k = ['apple', 'mango', 'banana']
for i in k:
    print("index: ", k.index(i))
    print("value: ", i)

print("-------\n")

k = ['apple', 'mango', 'banana']
for i in range(len(k)):
    print("index: ", i)
    print("value: ", k[i])

print("-------\n")

t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(type(t))
print(dir(t)) #Bu class ile yapabileceğin komutları gösteriyor.

print("-------\n")

stuff = list() #veya [] yazarak boş bir liste oluşturabilirsin
stuff.append("Book")
stuff.append(99)
stuff.append(input("Eklemek istediğini yaz > "))
print(stuff)

print("-------\n")

some = [1,9,21,10,16,3,41,12,74,15]
print(some)
some.sort()
print(some)
print("[2] is ",some[2])
print("Len ", len(some))
print("Max ", max(some))
print("Min ", min(some))
print("Sum ", sum(some))
print("Sum/Len ", sum(some)/len(some))

print("-------\n")

isimler = ["Ali", "Veli", "Ahmet", "Mehmet"]
print(isimler)
isimler.sort()
print(isimler)

print("-------\n")

print("Average Calculator\n")

#1.Yol
total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    total = total + value 
    count += 1 
average = total / count
print("Birinci yol ile ortalama ", average)

#2.Yol
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("İkinci yol ile ortalama ", average)
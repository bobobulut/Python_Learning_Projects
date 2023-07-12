d = {"a":10, "b":1, "c":22}
print(d.items())
print(sorted(d.items()))

print()

t=sorted(d.items())
print(t)

print()

for k,v in sorted(d.items()):     
   print(k,v)

print("--------\n")

c = {"a":10, "b":1, "c":22}
tmp = list()
for k,v in c.items():
   tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

print("--------\n")

counts = {"a":10, "b":1, "c":22}
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print() #yukarıdaki ile aşağıdaki kod aynı işlevi görüyor

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

print("--------\n")

fhand = open("/Users/borayazgan/Documents/Visual Studio Projects/Files/Test.rtf")
counts = dict()
for line in fhand:
   words = line.split()
   for word in words:
      counts[word] = counts.get(word,0) + 1

lst=list()
for key,val in counts.items():
   newtup = (val,key)
   lst.append(newtup)

lst = sorted(lst, reverse = True)
for val, key in lst [:10]:
   print(key, val)


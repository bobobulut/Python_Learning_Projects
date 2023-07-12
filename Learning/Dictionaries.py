purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)

print()

print(purse["candy"])
purse["candy"] = purse["candy"] + 2 
print(purse["candy"])
print(purse)

print("--------\n")

jjj = {"chuck":1, "fred":42, "jan":100}
ooo = {}
print(jjj)
print(ooo)

print("--------\n")

print("1.Yol")

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

print()

print("2.Yol")

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    counts[name] = counts.get(name, 0) + 1  
print(counts)
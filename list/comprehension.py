fruitname = ["Cherry","Banana","apple","Mango"]
newlist = []
for i in fruitname:
    if "a" in i:
        newlist.append(i)
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
for i in fruitname:
    if i != "Banana":
        print(i)

fruitname = ["Banana","Apple","Cherry"]
newlist = [x for x in fruitname if x != "Cherry"]
print(fruitname)
print(newlist)

newlist = [x for x in range(19)]
print(newlist)

newlist = [x for x in range(12) if x < 5]
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
newlist = [x.upper() for x in fruitname]
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
newlist = [x.lower() for x in fruitname]
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
newlist = ["Cherry" for x in fruitname]
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
newlist = [x if x != "Banana" else "Apple" for x in fruitname]
print(newlist)

fruitname = ["Banana","Apple","Cherry"]
newlist = [x for x in fruitname if x == "Cherry"]
print(newlist)
fruitname = ["Cherry", "Banana", "Apple", "Mango"]
newlist = []

for i in fruitname:
    if "a" in i.lower():  # Using .lower() to handle case insensitivity
        newlist.append(i)

print(newlist)

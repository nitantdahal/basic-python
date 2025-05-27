fruitname = ["Cherry","Banana","Apple"] # Normal list program
print(fruitname)

fruitname = ["Cherry","Banana","Apple"] # Length of items in fruitname variable
print(len(fruitname))

fruitname = (("Cherry","Banana","Apple")) # Store items inside small braces
print(fruitname)

fruitname = ["Cherry","Banana","Apple"] # data type 
print(type(fruitname))

fruitname = ["Cherry","Banana","Apple"] # indexed selection 1 
print(fruitname[1])

fruitname = ["Cherry","Banana","Apple"] # Negative indexing
print(fruitname[-1])

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # Range of item selection
print(fruitname[1:4])
print(fruitname[:4])
print(fruitname[1:])
print(fruitname[-5:-2])

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # included in list or not
if "graphes" in fruitname:
    print("Yes, graphes is included in list.") 
else:
    print("No, graphes is not included in list.")

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] #insert new item
fruitname.insert(4,"watermelon")
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # add item at last of the list
fruitname.append("waterfruit")
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # add item of one variable to another
number = [1,2,3,4,5,6,7,8,9]
number.extend(fruitname)
print(number)

fruitname = ("Cherry","Banana","Apple","Kiwi","Guava","Orange") # add item of one var to another (which is tuple)
number = [1,2,3,4,5,6,7,8,9]
number.extend(fruitname)
print(number)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # remove item from the list
fruitname.remove("Apple")
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # delete "Banana"
fruitname.pop(1)
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # delete "Cherry"
del fruitname[0]
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # delete entire list
del fruitname

fruitname = ["Cherry","Banana","Apple","Kiwi","Guava","Orange"] # add item at last of the list
fruitname.clear()
print(fruitname)

fruitname = ["Cherry","Banana","Apple","Mango"]
newlist = []
for "a" in i:
    newlist.append(i)
    print(newlist)
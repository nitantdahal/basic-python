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
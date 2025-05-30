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

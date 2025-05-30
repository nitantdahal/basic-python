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

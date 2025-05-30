thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #You can also use discard() instead of remove()
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
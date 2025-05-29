x = ("Dhoni","Kohli","Raina")
y = list(x)
y[2] = "Rohit"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

x = (1,2,3)
y = (4,5,6)
x += y
print(x)

x = ("Muktiraj","Kumar","Dahal")
y = list(x)
y.remove("Kumar")
x = tuple(y)
print(x)
def my_name(): # simple use of function
    print("My name is Mukti")

my_name()

def my_name(fname, lname): # Two Parameters
    print(fname + " " + lname)

my_name("Muktiraj", "Dahal")

def my_name(*name): # using * in storing multiple arguments
    print("My name is" + " " + name[1])

my_name("Muktiraj", "Nitant", "Nischal")

def my_name(fname, sname, tname): # using dictionary
    print("The oldest children name is " + sname)

my_name(fname = "Muktiraj", sname = "Nitant", tname = "Nischal")

def my_function(**kid): # using ** in dictionary cases
  print("His last name is " + kid["lname"])

my_function(fname = "Nitant", lname = "Dahal")

def country(country = "Nepal"): # Default parameter value
    print("I am from " + country)

country()

def my_function(fnames): # Passing a List as an Argument
    for x in fnames:
        print(x)

lnames = ["Dahal","Basnet", "Karki"]

my_function(lnames)

def my_function(x): # Return Values
    return 7 * x

print(my_function(5)) 
print(my_function(6)) 
print(my_function(7)) 
print(my_function(8)) 
print(my_function(9)) 

def my_function(): # The pass Statement
    pass
    
# Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

# def my_function(x, /): (Error)
#   print(x)

# my_function(x = 3)

# Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)

# def my_function(*, x): (Error)
#   print(x)

# my_function(3)

def my_function(a, b, /, *, c, d): # Combine Positional-Only and Keyword-Only
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k): # Recursion
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

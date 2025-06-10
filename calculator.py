print("Select Operation First:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter a choice (1/2/3/4): ")

if choice == '1':
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Addition: ", a + b)

elif choice == '2':
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Subtraction: ", a - b)

elif choice == '3':
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Multiplication: ", a * b)

elif choice == '4':
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    if b == 0:
        print("Indeterminate form, i.e. Not Valid")
    else:
        print("Division:", a / b)
else:
    print("Invalid values")






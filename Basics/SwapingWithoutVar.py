#Swapping Without Variables
a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
a = a + b
b = a - b
a = a - b
print(f"After Swapping a = {a} b = {b}")
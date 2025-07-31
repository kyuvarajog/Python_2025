#To Find Maximum Number Between 2 numbers
a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
if(a>b):
    print(f"The Number {a} is greater than {b}")
elif(a<b):
    print(f"The Number {b} is greater than {a}")
else:
    print(f"Both Number's {a} and {b} are same")
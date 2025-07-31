#Find Maximum Between Three Variables
a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
if(a>b and a>c):
    print(f"The largest of the three is: {a}")
elif(b>a and b>c):
    print(f"The largest of the three is: {b}")
elif(c>a and c>b):
    print(f"The Largest of the three is: {c}")
elif(c==a and c==b):
    print(f"All The Three Number's are same")
elif(a>b and b==c):
    print(f"The Largest of the three is: {a} but {b} and {c} are same")
elif(b>a and b>c and a==c):
    print(f"The largest of the three is: {b} but {a} and {c} are same")
elif(c>a and c>b and a==b):
    print(f"The largest of the three is: {c} but {a} and {b} are same")
else:
    print("Invalid Input")
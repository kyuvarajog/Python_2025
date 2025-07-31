#Getting a student's Name and Average and Deviation
name = input("Enter the student's name: ")
S1 = int(input("Enter First Subject Marks: "))
S2 = int(input("Enter Second Subject Marks: "))
S3 = int(input("Enter Third Subject Marks: "))
Total = S1 + S2 + S3
Avg = Total / 3
Dev1 = Avg - S1
Dev2 = Avg - S2
Dev3 = Avg - S3
print(f"Hi {name}, Total Marks: {Total}, Average: {Avg}\n")
print(f"Deviation 1: {Dev1}\n Deviation 2: {Dev2}\n Deviation 3: {Dev3}\n")
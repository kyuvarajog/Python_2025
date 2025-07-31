#input Student Name and 3 Subject and calculate average
name = input("Enter Student Name: ")
s1 = input("Enter Marks for Subject 1: ")
s2 = input("Enter Marks for Subject 2: ")
s3 = input("Enter Marks for Subject 3: ")
Total = int(s1) + int(s2) + int(s3)
Per = (Total / 300) * 100
print("Student Name: Total Marks: " + name + " " + str(Total) + " Percentage: " + str(Per) + "%")
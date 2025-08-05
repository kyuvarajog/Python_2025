Basic_Salary = float(input("Enter your Salary: "))
Years_of_Service = int(input("Enter your Years of Service: "))
Overtime_Hours = int(input("Enter your Overtime Hours: "))
Department_Code = input("Enter your Department Code (Integer: 1 → HR, 2 → IT, 3 → Sales, 4 → Finance): ")
if Basic_Salary <= 25000:
    Tax_Rate = 0
elif Basic_Salary <= 50000 and Basic_Salary > 25000:
    Tax_Rate = 5
elif Basic_Salary <= 100000 and Basic_Salary > 50000:
    Tax_Rate = 10
if Years_of_Service < 1:
    Bonus = 0
elif Years_of_Service <= 5 and Years_of_Service >= 1:
    Bonus = 5000
elif Years_of_Service <= 10 and Years_of_Service > 5:
    Bonus = 10000
elif Years_of_Service > 10:
    Bonus = 20000
if Overtime_Hours >=1 and Overtime_Hours <=5:
    Rate_per_Hour = 100
elif Overtime_Hours >5:
    Rate_per_Hour = 150
if Department_Code == "1":
    Allowance = 3000
elif Department_Code == "2":
    Allowance = 5000
elif Department_Code == "3":
    Allowance = 4000
elif Department_Code == "4":
    Allowance = 4500
Total_Salary = Basic_Salary + (Overtime_Hours * Rate_per_Hour) + Bonus + Allowance
Tax = (Total_Salary * Tax_Rate) / 100
Net_Salary = Total_Salary - Tax
print("Your Net Salary is: ", Total_Salary)
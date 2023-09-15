#Course Outline
  #Week 1 (Setp 9, 2023)
    #Module 1 Intrduction to Python Progamming Essentrials Training
    #Module 2 Strings and Conditions
  #Week 2 (Sept 16,2023)
    #Module 3 Sttructures, Sequence and Selection
    #Module 4 Iteration
  #Week 3 (Sept 23, 2023)
    #Assessment #1, Module 5 Functions
    #Module 6 Tuple
  #Week 4 (Sept 30, 2023)
    #Module 7 Exceptions and blocks
    #Module 8  Objects
  #Week 5 (Oct 7, 2023) 
    #Assessment #2, Module 9 File handling
    #Hands-on Assessment, Closing Ceremony

#------------------------------------------------------------------------------------------------------
  #Week 1 (Setp 9, 2023)
    #Module 1 Intrduction to Python Progamming Essentrials Training
    #Module 2 Strings and Conditions

#Day 1 Act 1
first_name = "Christian"
last_name = "Espinosa"
hours_worked = 8
rate_per_hour = 100
deduction = 5

print("Firstname:",first_name)
print("Lastname:",last_name)
print("Hours Worked",hours_worked)
print("Rate per hour:",rate_per_hour)
print("Deduction:",deduction)

#Day 1 Act 2
first_name = input("Enter First Name: ")
last_name = input("Enter last Name: ")
hours_worked = int(input("Enter Hours Worked: "))
rate_per_hour = int(input("Enter Rate per hour: "))
deduction = int(input("Enter Deduction: "))
salary = hours_worked * rate_per_hour - deduction

print("Firstname:",first_name)
print("Lastname:",last_name)
print("Hours Worked",hours_worked)
print("Rate per hour:",rate_per_hour)
print("Deduction:",deduction)
print("Salary: ",float(salary))


#Day 1 Act 3
noun1 = input("Enter the first noun: ").upper() # Jhon
noun2 = input("Enter the second noun: ").upper() # Porridge
adjectives1 = input("Enter the first adjectives: ").upper() # Cooking
adjectives2 = input("Enter the second adjectives: ").upper() # delicious
original_poem = "You go home one evening tired from work,\nand your mother boils you a turtle soup. \nTwelve hours hunched over the hearth"

print("\nOriginal Poem\n"+original_poem)
print("\nResult")
print(original_poem.replace("your mother",noun1).replace("boils",adjectives1).replace("turtle",adjectives2).replace("soup",noun2))

#Day 1 Act 4  Assignment
employee_name = input("Employee Name: ")
no_of_hours = int(input("Enter number of hours: "))
sss = int(input("SSS contribution: "))
phil_health = int(input("Phil health: "))
housing_loan = int(input("Housing Loan: "))
rate_per_hour = 500
gross_salary = no_of_hours * rate_per_hour
tax = gross_salary * 0.1
total_deduction = sss + phil_health + housing_loan + tax
net_salary = gross_salary - total_deduction

print("==========PAYSLIP==========")
print("==========EMPLOYEE INFORMATION==========")
print("Employee Name:", employee_name.upper())
print("Rendered Hours:", no_of_hours)
print("Rate per Hour:", rate_per_hour)
print("Gross Salary:",float(gross_salary))
print("==========DEDUCTIONS==========")
print("SSS:", sss)
print("PhilHealth:", phil_health)
print("Other Loan:", housing_loan)
print("Tax:", tax)
print("Total Deductions:", total_deduction)
print("")
print("Net Salary:PHP", net_salary)
#------------------------------------------------------------------------------------------------------
  #Week 2 (Sept 16,2023)
    #Module 3 Sttructures, Sequence and Selection
    #Module 4 Iteration














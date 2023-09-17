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

## Day2 Act 1

name = input("Enter your name: ")
math = float(input("Enter your math grade: "))
sci = float(input("Enter your science grade: "))
eng = float(input("Enter your english grade: "))
average =int((math + sci + eng)/3)

print(f"Your average is {average}")
if average >= 75:
    print("Congratulations! You passed the semester.")
    if math < 75:
        print("But you need to re-enroll to re-enroll Math subject")
    elif sci < 75:
        print("But you need to re-enroll to re-enroll Science subject")
    elif eng < 75:
        print("But you need to re-enroll English subject")
else:
    print("You failed the semester.")

##Day2 Act2

office = input("Enter your office department [it, acct, hr]: ")
year_in_service = int(input("Years in service: "))

if office == "it" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving it department for more than 10 years is 10000")
elif office == "it" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving it department below 10 years is 5000")
elif office == "acct" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your Incentives for serving acct department for more than 10 years is 12000")
elif office == "acct" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving acct department below 10 years is 6000")
elif office == "hr" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your Incentives for serving hr department for more than 10 years is 15000")
elif office == "hr" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving hr department below 10 years is 7500")
else:
    print("Invalid input")

## Day2 Act3

msg = 1

while msg <= 20:
    print(f"Python while loop number {msg}")
    msg +=1














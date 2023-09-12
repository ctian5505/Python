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

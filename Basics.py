#Vriables, Print and Input

#Just a basic code for getting monthhly Salary and Savings per month
yearly_salary = int(input("Enter your Yearly salary")) #input always string
savings = yearly_salary*0.2
Monthly_salary = round(yearly_salary/12)

print(f"Monthly Salary = {Monthly_salary}")
print(f"Yearly Savings = {savings}")

#
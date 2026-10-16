Message = ("Let's see how much hours you need to work for your budget!") # The program will ask you for your hourly wage and your expenses: Rent, groceries, internet bill , and extra money for fun allowance
print(Message)                                                  
Hourly_wage = float(input("Enter your hourly wage:"))   
Rent_amount = float(input("Enter your  monthly rent amount:"))
Internet_service = float(input("Enter your monthly Internet bill:"))
Groceries_amount = float(input("Enter your monthly groceries amount:"))
Fun_allowance = float(input("Enter your monthly fun allowance:")) 
Monthly_expenses = (Rent_amount + Internet_service + Groceries_amount + Fun_allowance)     # The program will add all of the amount of these expenses together


print(Monthly_expenses)
Month_hours = (Monthly_expenses // Hourly_wage)  # The program will divide monthly expenses by the hourly wage to see how mnay hours they have to work the whole month
print(Month_hours)
Week_hours = (Month_hours // 4) # The program will divide the monthly hourd by 4 for week in a month  to see how many hours per a week

print(Week_hours)
Savings_= (Monthly_expenses + 100)   # The program will add 100 to the montly expesnes 

print(Savings_)
New_savings = (Savings_ // Hourly_wage)       # Then it will divde the savings by the hourly wage 
print(New_savings)
Monthly_savings = (New_savings // 4)        # Then it will divide the that result by 4
print(Monthly_savings)


print("Hourly wage: ", Hourly_wage)
print("Monthly expenses: ", Monthly_expenses)                             # The answer will show all the answers the user needs
print("Monthly hours needed to for expenses:", Month_hours)
print("You need to work 2 more hours per a week for savings")
print("Weekly work hours neeed to reach goal is: ,", str(Week_hours + 2))


monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings with 5% interest 
interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)


print("Projected savings after one year, with interest, is: $", (projected_savings))
print("Your monthly savings are $", (monthly_savings))


# The user is prompted to enter their monthly income and expenses, and the code calculates the monthly savings. 
# It also includes a 5% interest rate on the total savings.  
   

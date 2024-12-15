monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = float(monthly_income - total_monthly_expenses)

# Calculating the projected savings after one year, incorporating the interest
projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Printing the user's monthly savings and projected annual savings after including interest
print("Your monthly savings are ${}".format(monthly_savings))
print("Projected savings after one year, with interest, is: ", projected_savings)
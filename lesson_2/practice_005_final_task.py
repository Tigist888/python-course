# Create a program that will calculate your monthly expenses.
# Each expense amount is represented by a variable.

rent = 1200
utilities = 300
groceries = 450
entertainment = 200

# Calculate the total monthly expenses and determine the
# percentage of rent relative to the total expenses.
total_monthly_expanse=rent+utilities+groceries+entertainment
print(total_monthly_expanse)
rent_perentag=(rent/total_monthly_expanse)*100
print(rent_perentag)

# Hint: to count the percentage of rent, count total monthly
# expenses first, then divide expenses for rent by the total
# expenses and multiply by 100.

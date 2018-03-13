"""
Program to calculate and display a user's bonus based on sales
If sales are under $1,000, the user gets a 10% bonus
If sales are over  $1,000, the bonus is 15%
"""

sales = float(input("Enter Sales Amount: $ "))
if sales >=1000:
    bonus = 0.15 * sales
else:
    bonus = 0.10 * sales

bonus = int(bonus)

print("Bonus :$",bonus)


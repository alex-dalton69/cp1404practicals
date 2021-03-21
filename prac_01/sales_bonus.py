"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        print("The bonus is 15%: $", sales * 0.15)
    else:
        print("The bonus is 10%: $", sales * 0.1)
    sales = float(input("Enter sales: $"))
else:
    print("You have lost the company money, you are fired.")




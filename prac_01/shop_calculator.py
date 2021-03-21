total_price = 0
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid numner of items!")
    num_items = int(input("Number of items: "))
for i in range(num_items):
    item_cost = float(input("Price of item: "))
    total_price = total_price + item_cost
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print("Total price for {} items is ${:.2f}".format(num_items, total_price))

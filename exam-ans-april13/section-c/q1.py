# A shopkeeper wants to calculate the total bill:
# 1. Take price and quantity as input
# 2. Calculate total cost
# 3. Apply 10% discount if total > 1000


price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

# total cost
total_cost = price * quantity

if total_cost > 1000:
    discount = (10 / 100) * total_cost
    print("Discount applied..!", discount)
    print("Total bill: ", total_cost)
    total_cost -= discount
    print("After discount: ", total_cost)
else:
    print("Total Bill: ", total_cost)

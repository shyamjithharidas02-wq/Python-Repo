# ATM system:
# Take balance and withdrawal amount
# Check if sufficient balance is available


balance = 2500
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount <= balance:
    balance -= amount
    print(f"{amount} credited from your account")
    print("Remaining Balance: ", balance)
else:
    print("Not enough balance!. Please try again later")

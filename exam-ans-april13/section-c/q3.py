# A mobile app asks users to enter age:
# If age < 18 → “Not eligible”
# Else → “Eligible to vote”


age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible")
else:
    print("Eligible to vote")

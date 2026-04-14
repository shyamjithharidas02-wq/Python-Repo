# Write a program to print the multiplication table of a given number.

number = int(input("Enter a number to generate multiplication table (to 10): "))
limit = 10

for i in range(1, limit + 1):
    print(f"{i} x {number} = {i*number}")

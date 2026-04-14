# Write a program to find the factorial of a number using a while loop.

number = int(input("Enter a number to find factorial: "))

i = 1
fact = 1

while i <= number:
    fact *= i
    i += 1


print(f"factorial of {number} is {fact}")

# Write a program to calculate the sum of first N natural numbers.

sum = 0
n_number = int(input("enter n natural number: "))

for i in range(n_number + 1):
    sum += i

print(f"sum of {n_number} n natual number is: {sum}")

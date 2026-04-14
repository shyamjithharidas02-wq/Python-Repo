# Write a program to print:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

row = int(input("Enter row count: "))

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

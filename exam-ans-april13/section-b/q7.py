#  left angle tri-angle
# *
# * *
# * * *
# * * * *
# * * * * *

row = int(input("Enter row count: "))

for i in range(1, row + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Write a program to find the second largest number in a list.


# type 1
numbers = [10, 30, 90, 101, 91, 91, 100, 20, 18]
numbers.sort()
print(f"second largest number is: {numbers[-2]}")

print()

# key case:
# if a list contain two duplicate numbers can not find second largest then:
#  eg: [10,20,30,40,50,50]
# in this case second largest number is again 50, so in this edge case remove the duplicate and then:
# 1. remove duplicate element
# 2. find second largest

# type 2
number_list = [10, 30, 90, 101, 91, 91, 100, 20, 18]
largest = second_largest = float("-inf")

for num in number_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"second largest number in this list is: {second_largest}")

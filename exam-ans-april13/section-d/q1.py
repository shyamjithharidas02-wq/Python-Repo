# Write a program to remove duplicate elements from a list.

# type 1
number_list = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8]
unique_numbers = list(set(number_list))
print(unique_numbers)


print()
# type 2
number_list1 = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8]
unique_list = []

for num in number_list1:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)

# Write a program to count how many even and odd numbers are present in a list.

# type 1
number = int(input("Enter a number to generate a list: "))
list1 = []

for i in range(1, number + 1):
    list1.append(i)

print(list1)
even_count = 0
odd_count = 0


for j in range(len(list1)):
    if list1[j] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"even count: {even_count}")
print(f"odd count: {odd_count}")


print()
# type 2
number1 = int(input("Enter a number to generate a list: "))
gen_list = list(range(1, number1 + 1))

e_count = o_count = 0

for n in gen_list:
    if n % 2 == 0:
        e_count += 1
    else:
        o_count += 1

print(f"Generate list: {gen_list}")
print(f"Odd count: {o_count}")
print(f"Even count: {e_count}")

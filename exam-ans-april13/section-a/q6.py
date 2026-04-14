# Write a program to perform basic arithmetic operations (+, -, *, /) based on user choice.

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

user_choice = input("Enter choice:\n+, -, *, / :\n")

match user_choice:
    case "+":
        print(first_num + second_num)
    case "-":
        print(first_num - second_num)
    case "*":
        print(first_num * second_num)
    case "/":
        print(first_num / second_num)
    case _:
        print("Invalid choice!. Please choose from a given option")

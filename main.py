#very simple pyhton calculator bc im beginner

operator = input("Choose Your Operation (+ - * /) =")

num1 = float(input("Enter the first number ="))
num2 = float(input("Enter the second number ="))


if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is an invalid operator!")
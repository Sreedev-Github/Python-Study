# Problem: Create a function that takes two numbers as parameters and returns their sum.

number1 = int(input("Give us a number: "))
number2 = int(input("Give us a another number: "))

def sum_of_numbers(num1, num2):
    return num1 + num2

result = sum_of_numbers(number1, number2)

print(f"The sum of {number1} and {number2} is {result}")
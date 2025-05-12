# Problem: Create a lambda function to compute the cube of a number.

# A lambda function, also known as an anonymous function or lambda expression, is a concise way to define a small, single-use function in Python.

number = int(input("Please provide a number: "))

number_cube = lambda num : num ** 3

print(number_cube(number))
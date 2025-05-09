# roblem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# Accept both string por number values from the user
value = 5

number = int(input("Enter the number to multiply the value with: "))

def multiply(value, number):
    return value * number

result = multiply(value, number)
print(f"The result of multiplying {value} with {number} is: {result}")
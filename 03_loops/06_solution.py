# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

# Factorial formula = number = 5... 5*4*3*2*1

number = 5
factorial = 1

# While loop
while number > 0:
    factorial *= number
    number -= 1

print("Factorial value is", factorial)





# Did by me by for loop

# number = 10
# factorial__num = 1
# for i in range(1, number+1):
#     factorial__num *= i

# print(factorial__num) 
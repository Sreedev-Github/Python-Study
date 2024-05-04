# 8. Prime Number Checker
# Problem: Check if a number is prime.

# Prime number = Only divisible by 1 and itself

number = 10

is_prime = True # Storing random value as of now as we will change the Boolean value based on equation

if number > 1:
    for i in range(2, number): # Here we are not ging number-1 in range as we know it will surely be divisible by the number itself
        if (number % i) == 0:
           is_prime = False
           break;
else:
    print("Please enter a number greater than 1")

print(is_prime)
# Problem: Create a recursive function to calculate the factorial of a number.

# what is facotorial
# 1. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# example: Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120


# Recursive Function
# 1. A recursive function is a function that calls itself to solve smaller instances of the same problem.
# 2. It has a base case to stop the recursion and a recursive case to call itself with a smaller input.
# 3. The base case is the condition under which the function stops calling itself.
# 4. The recursive case is the part of the function that calls itself with a smaller input.
# 5. Recursive functions can be less efficient than iterative solutions due to function call overhead.


# Exit strategy is important in recursive function
def factorial(n):
    if n == 0:
        return  1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
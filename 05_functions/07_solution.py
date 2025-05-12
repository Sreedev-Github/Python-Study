# Problem: Write a function that takes variable number of arguments and returns their sum.

# Means that we can have an function which can have n number of arguments

# You must use *args when you are accepting multiple parameters and not use any other keywords, anything with a * will work but it is not considered ideal.

def sum_all(*args):
    # print(args) # Returns a Tuple which holds all the values

    # We can loop thorugh tuples
    for i in args:
        print(f"current value of i is {i}")

    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4))


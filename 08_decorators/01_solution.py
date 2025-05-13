# Decorator which meausres a time required for a function to run

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # __name__ helps get the name of the function that has been passed
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

# The "@timer" acts as a decorator so this below function won't run as it is, inestead it is passed to the timer definition with it's parameters too.

@timer
def example_function(n):
    time.sleep(n)

example_function(2)






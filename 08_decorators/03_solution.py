# Cache Return Value
# A decorator which cached value of the last return value, so that if a same paramters are passwed, it can used the cached values.

import time

def cache(func):
    # Create a dictiornary 
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        # If the args are same as the last call, then return the cached values
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4) # Suppose this is a long database call
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))

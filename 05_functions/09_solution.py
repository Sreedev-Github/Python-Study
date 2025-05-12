# Problem: Write a generator function that yields even numbers up to a specified limit.

# How I though of doing it
# def even_generator(limit):
#     n = 0
#     while limit > n:
#         if n % 2 == 0:
#             print(n)
#             n+=1
#         else:
#             n+=1
            


# even_generator(100)


# Easy way using Range as it accepts a step parameteras well

# def even_generator(limit):
#     for i in range(2, limit +1, 2): # Skips 2 numbers , which also includes the current number so we use 2
#         print(i)

# even_generator(10)


# Yielding means generate and not return
# When you use yeild here isntead of return, it will sotrage the reference of the state of the function so if the first returned value was 2 then the next will be 4. And it will store different reference for each different loops.

# Explain yielding : # 1. When you use yield, the function becomes a generator.
# 2. The state of the function is saved, so when you call next() on the generator, it resumes from where it left off.
# 3. This is useful for generating a sequence of values without storing them all in memory at once.
# 4. You can use a for loop to iterate over the generator, which will automatically call next() for you.
# 5. Generators are memory efficient because they yield one value at a time instead of returning a list of values.
# 6. You can use the next() function to get the next value from the generator.
# 7. When the generator is exhausted, it raises a StopIteration exception.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i 

    
for num in even_generator(10):
    print(num)


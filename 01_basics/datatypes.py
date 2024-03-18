# So everything in python is considered to be an object, so it's okay to say Datatypes Objects

# ---------------------------- Numbers -----------------------------

# Basic maths calculations
print(12 + 12)

# Python priortizes decimal values so if your calculation has any decimal numbers the output will also be in decimals
print(2.5 + 12.5)

# Python is good with numbers unlike JS so it can handle quite large numbers easily 
print(2 ** 100)

#  We can import Math library for more options with numbers
import math
print(math.pi)

# We can use this random library which works as math.random in JS but with a bit more functionality, like this random.choice below
import random
print(random.random())
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



# ---------------------------- Strings -----------------------------

username = 'Hello World'

# We use this len property to check it's length 
print(len(username))

# As we know strings indexes can also be accessed just like in list so we can call an certain character using the index
print(username[9])

# If you give the index in minus values then the index is calculated from the end of the string
print(username[-3])

# username[0] = 'A' .... We can do this and change an certain value in list but we can't do that here as if we remember strings are immutable so we cannot edit the string, but only replace it with another value

# This way you can access indexes from a start of end of the given indexes, however the last given number's index is not included, so here we are only getting the values from 0 to 4
print(username[0:5])

# This dir gives us all the different prototypes which we can use in strings so we get an idea of which all can we use in the given datatype
# print(dir(username)) # commenting this out as there's alot of text coming in the terminal


# ---------------------------- List (Array) -----------------------------

mylist = [123, "hello", 3.14]
print(mylist)

# You can check the length just as you did for the string
# But the catch is the length here starts from 1 and not 0
print(len(mylist))

# Gives the value of the 0th index of the list
print(mylist[0])

# Gives the value of the first index from the last of the list
print(mylist[-1])



# ---------------------------- Tuple -----------------------------

# Research the difference between Tuple and List on your own, however something to know is mostly we use list in our day to day work
myTup = (1, 2, 4)
print(myTup[0])
print(len(myTup))




# ---------------------------- Dictionary (objects) -----------------------------

myDict = {'one': 'apple', 'two': 'mango', 'three': 'banana'}
print(myDict)

# Works as objects, prints the value of the given key
print(myDict['three'])

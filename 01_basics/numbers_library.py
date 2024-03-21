# Python has number precision so no matter how big of a number you give it will return the correct value unlike in other languages where you might get exponential values or 10 > 5

import math
import random


# Floor returns the closest lowest value of the given number
print(math.floor(3.9)) # 3
print(math.floor(-3.9)) # -4

# Trunc always takes you towards 0 no matter if it's a positve or negative number
print(math.trunc(3.1))
print(math.trunc(-3.9))

# These are iota numbers.. also known as complex numbers which people might need in Data Science or fields like that but they serve little to no purpose in web dev 
print((2 + 1j) * 3)


# Learn more about all these 
# Octal Literal
print(0o20)

# Hexal Literals
print(0xFF)

# Binary Literals
print(0b1000)

# Bitwise.. For competative progarming.. No notes on these



# Random Library

random.random() # Gives random numbers between 0 to 100 jus like Math.random() in JS

# But unlike in JS where we have to give some calculations to get random numbers between a set of numbers like Math.random()*100 +1.. This gives use number between 1 to 100
# We can easily do this in python
print(random.randint(1, 10)) # Gives us random numbers from 1 to 10


# Random Choice
l1 = ['apple','mango', 'banana', 'grapes']
print(random.choice(l1)) # Gives a random element from the give list



# Random Shuffle
# The random.shuffle() function in Python shuffles the elements of a list in place. Instead of returning the shuffled list, it directly modifies the original list. 
random.shuffle(l1) # Shuffles the list
print(l1)


# Decimals
# Decimal issue in Python
print(0.1 + 0.1 + 0.4) # Returns 0.6000000000000001.. which is acceptable

# However if you check this below statement you will be amazed
print((0.1 + 0.1 + 0.1) - 0.3) # This should return 0 as we would expect but it returns 5.551115123125783e-17


# We can solve this using a decimal library
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) # Prints 0.3
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # Prints 0.0

# If you wish to study more on this then you can study by searching "Decimal Context Manager"



# Fractions
from fractions import Fraction
myFra = Fraction(2, 7)
print(myFra) # Prints 2/7

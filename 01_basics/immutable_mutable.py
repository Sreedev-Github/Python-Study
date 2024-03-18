# Mutable Data Types in Python can be changed after decalration
# Examples are :- List, Set, Dictionary, Bytearray, Array

# Immutable Data types cannot be canged once they are declared
# Examples are :- Integers, Floating-point numbers, Boolean, Strings, Tuples, Frozen set, Bytes

username = "Sree"
print(username)

username = "Evy"
print(username)

# So here you see that the values have changed even though we say strings are immutable
# Waht happens here is when we named the username Sree it was pointing at Sree and when we redecalred it the value of username didn't change from Sree to Evy
# It instead created a new memory for Evy and points the username variable to Evy, So now as the value Sree is there without having anything pointing at it's value
# The python garbage collector will go and delete it to keep it smooth

x = 10
y = x
print(x)
print(y)

x = 15

print(x)
print(y)


# Read the above comment to get a easier understadning of this 
# So here what happens is when we declare a x variable with a value of 10 the new memory is created for the value 10 and then we point the variable y to the same value
# Pointing y to the same value means now both of the variable are not poiting to the same memory, then we redeclare the value of x to 15 so now the new memory is created for 15
# And now the x is pointing towards the memory which has the value 1 in it. But the value 10 won't be deleted by the python garbage collector as the variable y is still pointing at it
# So this way the values have been changed for the individual variable but the first meomory was never deleted
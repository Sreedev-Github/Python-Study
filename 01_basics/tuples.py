# Tuple is immutable whereas list are mutable
# We can change reference but can't change it's value.. just like strings

myTuple = ("Labrador", "Golden Retriever", "Beagle")
print(myTuple)

# Access value through index like in list
print(myTuple[0])

# Slicing also works just like in list
print(myTuple[1:])


# The feature in Tuple is that we can't update or add something to it's data
# myTuple[0] = "German Shepeard"
# Throws error = TypeError: 'tuple' object does not support item assignment

print(len(myTuple))
# Output - 3

# We can even add multiple tuples as well
more_breeds = ("German Shepeard", "Husky")
myNewTuple = myTuple + more_breeds # Order depends on what order you are giving here
print(myNewTuple)

# Questions
if "Husky" in myNewTuple:
    print("True, husky is in myNewTuple")


# Change reference
# We can't change values but we can reassign a new tuple to it just like we can reassign a string but not make changes on the already declared string
more_breeds = ("German Shepeard", "Husky", "Pitbull")
print((more_breeds))

# Check count of a value in tuple
print(myNewTuple.count("Husky")) # 1


# We sometimes get Tuples as data from database
# Destructuring tuple
myTuple2 = ("Labrador", "Golden Retriever", "Beagle")
(Labrador, Golden_Retriever, Beagle) = myTuple2
# It's necessary to make sure we are giving the same number of variables as the number of values in tuple
# So now the values have been store to individual variables
print(Golden_Retriever)


# Check typeof
print(type(Golden_Retriever))
print(type(myTuple2))


# Nested Stuple
myNestTuple = ("String1", (1, 2, 3), "String2")
print(myNestTuple[1][2]) # 3

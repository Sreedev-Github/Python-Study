# Python has number precision so no matter how big of a number you give it will return the correct value unlike in other languages where you might get exponential values or 10 > 5

# Python is very strong with numbers so it important to understand numbers here

x = 2
y = 3
z = 4

print(x+y)

# Python aslo has same mathamatical artithmathic equations like JS :- *, /, -, +, --, ++, **, %

# Always use brackets when you want to execute some calcualtion first and the other later.. You can sure be well aware of bodmass rule but you can't expect everyone to be
print(x + (z - y))


# It good to practice to make sure your both datatypes are equal, and by datatype I don't mean  number and string.. it could be float and int as well
print(40 + 2.23)
# Instead of this above code do the below one.. even though the output it just is a better practice
print(float(40 + 2.23)) # Use int when you don't want decimals and use float when you want decimals

# Basic concatination of strings
print('Hello' + 'World')


# print('Hello' + x) # Unlike in JS we cannot concatinate strings and number datatypes like this as it will throw an error


# You can give multiple variable like this 
print(x, y, z) # This generally returns us in () which we call as Tuple datatypes in Python
print(x+1, y*2) # This will also return the values in brackets which will be as (2+1, 3*2) = (3, 6)


print(y % 2) # Remainder calculator
print(z ** 2) # Power Calculator

print(2 ** 1000) # Python stands out here as many languages tend to fail doing some high maths calculation

#  repr(): It returns a string representation of the object. This representation is more detailed and often includes information such as the object's type and memory address. It's mainly used for debugging and development purposes.
print(repr('Hello'))

# str(): It returns a string representation of the object, but the representation is meant to be more human-readable. It's often used for display purposes when you want a cleaner representation of the object.
print(str('Hello2'))

# print(): This is the simplest form of printing a string, where you directly specify the string literal inside the print() function.
print('Hello3')


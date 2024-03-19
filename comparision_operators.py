# Comparision operators are :- >, <, ==, !, !=

# Comparision operators returns boolean values 
print(1<2)

print(4.0 == '4')

# You can use the same && ,  ||  operator in python in an easier way like this
# Also just like in JS you will get 1 boolean value based the result of both
print(10 == 10.0 and 5 > 2) # If any of them is false then it returns false
print(15 > 5 or 10 > 15) # If any of them is true then it returns true


# This here will be converted as (1 == 2 and 2 < 3).. So as the first equation itself returns false the whole statement is not false as this is a and statement so both of them have to be true
print(1 == 2 < 3)

# True and False have predifined values which is like True = 1 and False = 0
print(True == 1)
print(False == 0)

# However true is not 1 and similarly False is not 0, as True and the number 1 is stored differently

print(True + 4) # 1 + 4 = 5
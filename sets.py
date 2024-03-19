setone = {1, 2, 3, 4}

# Intersection
print(setone & {1, 3, 6, 4}) # Only returns the similar values in both the sets

# Union values
print (setone | {1, 3, 6, 4}) # Prints all the values but won't repeat any of them

# Differences
print (setone - {1, 3, 6, 4}) # Prints the vales which are not same in the set


# Even though you feel like this should return empty parenthesis but yet it will return set() as empty parenthesis refers to dict 
# Empty set is wrote as set()
print(setone - {1, 2, 3, 4})


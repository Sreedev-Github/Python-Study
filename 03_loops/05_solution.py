# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
my_str = "Hellooha"

# coverting the string to lowercase as the "H" and "h" will be seen differently
lowercase_str = my_str.lower()

for char in lowercase_str:
    if lowercase_str.count(char) == 1:
        print("Char is :", char)
        break; # This breaks the whole loop so once the first character is done then we break
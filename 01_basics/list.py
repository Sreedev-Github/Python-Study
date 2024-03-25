# List is just Array but it's better to call it List as you are working in Python

tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)

# You can print any particular item you need by using []
print(tea_varities[2]) 

# Slicing
print(tea_varities[1:3]) 
print(tea_varities[2:]) 
 
# Change values in a list
tea_varities[3] = "herbal"
print(tea_varities)
# If you want to change it using slicing dicing then you will have to send the values in list or else it will add individual characters in the list
# You can also change multiple items if you wish to like this
tea_varities[1:2] = ["Lemon"] 
print(tea_varities)

# This will push the elements in the given number like as we have mentioned 1:1 so it will go past 0 but stay before 1
tea_varities[1:1] = ["test", "test"]
print(tea_varities)
# This removes as we are inserting nothing in there place so we can also say that this can be a deletion method
tea_varities[1:3] = []
print(tea_varities)


# Basic looping in list
# Make sure you keep an eye out for indentation as it plays a vital role in python
for tea in tea_varities:
    print(tea);

for tea in tea_varities:
    print(tea, end="-"); # Generally in print the default printings works with line breaks however we can change it using this end variable

print() # Printing a blank line as due to the end used above I was not getting a line break after that print and my output was something like "Black-Lemon-Oolong-herbal-Yes I have Black Tea"

if "Black" in tea_varities:
    print("Yes I have Black Tea")

# Append in list - Adds an value at the end of list
tea_varities.append("White")
print(tea_varities)

# Pop - Removes the last value
tea_varities.pop()
print(tea_varities)

# Remove a given value from the list
tea_varities.remove("herbal")
print(tea_varities)

# Add value in list
tea_varities.insert(1, "Green") # The first parameter tells it where to add this value and the second is the value itself
print(tea_varities)

# Cloning
# tea_varities_copy = tea_varities # If you do this then it will take the same reference instead of cloning
# This copy method copies the same list as it is. And any changes made to the main list after this won't affect this copy
# This will create a new list instead of refering to the same list as tea_varities had
tea_varities_copy = tea_varities.copy()
tea_varities_copy.append('White')
print(tea_varities)
print(tea_varities_copy)

# List comprehension
# We can do some complex calculations or insert codes in list unlike in other languages
# As you can see the x vairable is being declared here itself and then the loop runs changing the x value from 0 to 10
squared_num = [x**2 for x in range(11)] # Gave 11 as python doesn't include the given number but the numbers below it
print(squared_num)

cube_num = [x**3 for x in range(11)] # Gave 11 as python doesn't include the given number but the numbers below it
print(cube_num)
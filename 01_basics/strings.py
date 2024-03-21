text = "Hello World"
print(text)

# As we know strings indexes can also be accessed just like in list so we can call an certain character using the index
print(text[2])

# Convert the string to uppercase
uppercase_text = text.upper()
print(uppercase_text)

# Convert the string to uppercase
lowercase_text = text.lower()
print(lowercase_text)


# Replace method in strings.. It won't modify the original string.. So make sure to store it
print(text.replace("World", "Universe"))


# Remove extra spaces from the start and end of the text
text_spaced = "    Hello World    "
print(text_spaced.strip())


# Slicing in String
# Slice returns a new strings so you have to store it in a variable... Also it returns from the given index to a index before the last one
sliced_text =  text[0:5]
print(sliced_text)    # Output: Hello


# It's easy to understand slicing with a number list as you can see which number are coming
num_list = "0123456789"
print(num_list[:])   #
print(num_list[3:])   #
print(num_list[:7])   #

# There's a third parameter as well which does hopping.. Like if I have written 2 here that means it will only return every second index from 0 - 7
print(num_list[0:7:2])


# Split returns a new list
new_text = "text1, text2, text3, text4"
print(new_text.split()) # If you split without giving it any parameter then it will split based on the spaces in that strings
print(new_text.split(', ')) # now the comma and the space won't be included in the list


# Find  method - Returns first occurrence of the value
new_text2 = "Hello World"
print(new_text2.find("World"))


# RFind method - Returns the last occurrence of the value
print(new_text2.rfind("l"))


# Count method returns the number of counts of the given value in a text
print(new_text2.count("l"))


# Placeholder are the {} inside a strings like how we used in JS which were called template literals
# This method is called as formating
username = 'example1'
age = 25
country = 'USA'

info = "This user's username is {}, he is {} years old & he is from {}" # You leave the Placeholders blank as it it will be formatted later
print(info.format(username, age, country))

# Or this is an easier way of formatting where you mention f before the string
info2 = f"This user's username is {username}, he is {age} years old & he is from {country}"
print(info2)

# Join method
list1 = ["text1", "text2", 'text3', 'text4']
print(", ".join(list1)) # In this first parameter you give  what character or symbol will join your elements & second one is for the list

# Check length of the strings... Starts counting from 1
text3 = "Hello World"
print(len(text3))


# Basic for loop in strings
for char in text3:
    print(char)


# How to use quotes in quotes
# You can either use this single quotes and inside you can give double quote
text4 = 'He said, "python is the best programming language"'
print(text4)

# Or you can give this backslash to make sure that the code ignores the next quotes as a code and isntead renders it as a text
text5 = "He said, \"python is the best programming language\""
print(text5)

# At times you will have to use backslash in python while giving file directry so you can do it this way
# First let's see what can the error be
text6 = "windows\nuser"
print(text6) # So this returns the windows and file in different lines

# To avoid these kind of issue you can use r before the string which will let python consider it as a raw strings and won't make any changes to it
text7 =  r"c:\user\pwd"
print(text7)


# String containing Question
text8 = "Hello World"
# Returns a boolean, which will check if the mentioned value is there in the string or not... Case sensitive
print('Hello' in text8) 
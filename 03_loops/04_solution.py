# 4. Reverse a String
# Problem: Reverse a string using a loop.

my_str = "Python"

reversed_str = ""

for char in my_str:
    reversed_str = char + reversed_str

print(reversed_str)
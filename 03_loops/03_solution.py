# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Give me a number:"))

for i in range(1, 11):
    if i == 5:
        continue # skips the loop if i == 5
    print(number, 'x', i, '=', number * i)



# You can skip it like this as well but we are doing the above method to learn about the continue keyword
# for i in range(1, 11):
#     if i !=5: 
#         print(number, 'x', i, '=', number * i)
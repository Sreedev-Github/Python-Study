# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("Give a max number:"))

sum_even = 0

for i in range(1, number+1):
    if i % 2 == 0:
        sum_even += i

print(sum_even)
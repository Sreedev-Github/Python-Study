# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

# Set only keeps the unique values, whenever a duplicate comes in it won't take it in
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate", item)
        break
    unique_item.add(item)


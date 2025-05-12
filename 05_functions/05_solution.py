# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

name = input("Please share you name: ")

def greet_user(name):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello user")
    
greet_user(name)
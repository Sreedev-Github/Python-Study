# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# kwargs accepts key value pairs

# def pet_details(name, breed):
#     print("Name", name, "Breed", breed)

# pet_details(name="Evy", breed="Labrador", age=4, species="Dog")

# If the values in the paramter doesn't  match with the number of values being sent, then it will throw error in this way. This why we use kwargs


def pet_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


pet_details(name="Evy", breed ="Labrador", age=4, species="Dog")
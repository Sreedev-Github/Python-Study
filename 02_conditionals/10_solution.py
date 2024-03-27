# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "Dog"
age = 1

if pet == "Dog":
    if age <= 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif pet == "Cat":
    if age <= 2:
        food = "Kitten food"
    else:
        food = "Adult cat food"

print(food)
# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

#Commenting this input out as it is asking everytime I have to run the code
# age = int(input("Give an age: ")) 
age = 20

# if age < 13 :
#     print("Child")
# if age >= 13 and age < 20 :
#     print("Teenager")
# if age >= 20 and age < 60 :
#     print("Adult")
# if age >= 60 :
#     print("Senior")

# Other way of writing it would be using else if
# But here in python we write elif instead of else if

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
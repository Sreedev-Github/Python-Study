# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.



while True:
    user_value = int(input("Please give a number:"))
    if 1 <= user_value <= 10:
        print("Thank you!")
        break;
    else:
        print("Please try again")




    # if user_value <= 10 and user_value >= 1: #In python you can write this in short as written above in code
# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
# Not taking anymore input as it was just for us to learn
movie_age = 8
day =  "Wednesday"

# This is like the ternary operator so it's easy for us do this operation in one line
price = 12 if movie_age >= 18 else 8
if day == "Wednesday":
    price -= 2

print("Ticket price for you is $",price)
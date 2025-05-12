# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Circumference of a circle = 2 * pi * radius
# Area of a circle = pi * radius^2

radius = int(input("Enter the radius of the circle: "))

def circle_properties(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    print(f"The are of the square is {area} and it's circumference is {circumference}")


circle_properties(radius)

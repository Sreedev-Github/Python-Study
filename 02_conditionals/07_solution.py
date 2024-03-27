# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

cup_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = cup_size + " coffee with an extra shot"
else:
    coffee = cup_size + " coffee"

print(coffee)
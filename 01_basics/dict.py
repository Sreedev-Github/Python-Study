# Dict are like objects in JS

myDict = {
    "username": "Evy",
    "age":5,
    "breed":"labrador"
    }

# These are the two ways in which you can access the value of a key in Dict
print(myDict["username"]) #Evy
print(myDict.get("age"))

# Change or update a value of a given key
myDict["age"] = 5.5
print(myDict) 

# Iteration
for values in myDict:
    print(values)
# Output - It only prints keys
#  username
# age
# breed
    
# We do this to print values and keys 
# for values in myDict:
#     print(values, myDict[values])
# Output
# username Evy
# age 5.5
# breed labrador

# This is an easier syntax but in this we will have to make sure we add .items() after calling the dict as it will make sure to pass each item in it individually 
for key, value in myDict.items():
    print(key, value)



# Questions
if "breed" in myDict:
    print("Yes this Dict have breed name stored in it")


# Check length
print(len(myDict)) # Output - 3.. as There are 3 keys in it


# Add new key
myDict["color"] = "Golden Brown"
myDict["Random Value"] = "Will remove with pop"
print(myDict)


# Pop method - But you will have to pass the value as in Dict there is not sequence
myDict.pop("Random Value")
print(myDict)


# Pop items
myDict.popitem() # Remove the last item whatever it is.. here it removes color key and it's value
print(myDict)

# delete -Deletes the given key and it's value from the memory itself
del myDict["breed"]
print(myDict)


# Copy 
myNewDict = myDict.copy()
print(myNewDict)


# As we know we can make lists in list.. We can do same with Dict

animals = {
    "dog":{"breed1" : "Labrador", "breed2" : "Golden Retreiver", "breed3" : "Beagle"},
    "cat": {"breed1" : "Siamese", "breed2" : "Maine Coon", "breed3" : "Persian"},
    "bird": {"breed1" : "Parrot", "breed2" : "Canary", "breed3" : "Cockatiel"}
}

print(animals)

# Let's access a key which is inside a dict which again is inside another dict
print(animals["dog"]["breed2"]) # Golden Retreiver


# Maths in dict
# Just like in list we are running a loop but here we are giving it a key as well as you can see on x:x**2
squared_num = {x:x**2 for x in range(11)}
print(squared_num)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Remove all the key and values from the dict
squared_num.clear()
print(squared_num) # Returns empty parenthesis {}

# Lets try making a new dict with these values stored in list (array)
keys_list = ["breed1", "breed2", "breed3"]
value_list = "Labrador"

new_dict = dict.fromkeys(keys_list, value_list)
print(new_dict)
# {'breed1': 'Labrador', 'breed2': 'Labrador', 'breed3': 'Labrador'} Right now we are getting the same value in all the keys as we sent only 1 value

keys_list2 = ["breed1", "breed2", "breed3"]
value_list2 = ["Labrador", "Golden Retreiver", "Beagle"]
new_dict2 = dict.fromkeys(keys_list2, value_list2)
print(new_dict2)
# {'breed1': ['Labrador', 'Golden Retreiver', 'Beagle'], 'breed2': ['Labrador', 'Golden Retreiver', 'Beagle'], 'breed3': ['Labrador', 'Golden Retreiver', 'Beagle']}
# The output we get is not ideal as we can see instead of having 1 value, the keys have stored the value list itself in it...
# We will learn how to do it properply using loops later in this 
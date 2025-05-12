username = "Sree"

#This is a direct way of assigning a variable to memory. It gets created in the memory and reference is provided to it.

# Now comes scopes, often scopes are refered as {}, however you might not see {} so instead it works with : and indentations.

# The variables declared within functions stays within the function.


def func():
    username = "Chai"
    # Incase if the username is not found here then it keeps going up in the file, so if there's no username variable within the fucntion it will search in global.
    print(f"This print is insider the function, username:  {username}")


print(username) #Prints Sree
func()



x = 99

# def func2(y):
#     z = x + y
#     return z

# result2 = func2(1)
# print(result2)



def func3():
    global x # This makes sure we are using the variable from the global
    x = 88 # NOTE: We should not be using this as we are not supposed to change the global vairable value in a function


func3()
print(x)


# A fucntion inside the other function can access it's parent functions variables, just like how a function access global variales.
def f1():
    x = 78
    def f2():
        print(x)
    return f2 # returning the inner function means we are sending the whole reference to the f2 fuctions to whoever will call it.

myResult = f1()

# Closure
# This above example shows closures, so when a reference of the fucntion is sent it brings all the reference of the variable that is required along with it, and this is often known as closures.


def f2(num):
    def actual(x):
        return x ** num
    return actual

f = f2(2)
g = f2(3)


print(f"f function referece: {f}, g function reference: {g}") # This shows how both are stored in difference reference points in memory

print(f(3)) # Calculates square 3*3
print(g(3)) # Calculates cube 3*3*3

# As we have aready shared the parameter for calculating the square and cube while declaring f=f2(2) and g=f2(3).
# So this f and g is assigning values for the inner function parameter (num)
# This way we can unerstand how the inner function is carrying the parameter from the outer function.
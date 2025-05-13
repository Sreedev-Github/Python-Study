# Debugging function calls
# A function which helps us see how many arguments are being passed on the executed function

def args_finder(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}"for k, v in kwargs.items())
        print(f"Function name is: {func.__name__} and it has {args_value} agrs and {kwargs_value} kwargs.")
        return func(*args, **kwargs)
    return wrapper


@args_finder
def greet(firstName, lastName, greeting ="Hello"):
    print(f"{greeting} {firstName} {lastName}!")


greet("Sreedev", "Nair", greeting= "Hello there")
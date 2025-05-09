# Loops works like this :

# Iteration tool (looping tool like for loop, while loop, etc) makes a call to the iterator object
# The iterator object has two methods:
# 1. __iter__() : returns the iterator object itself and confims that ir can be iterated
# 2. __next__() : returns the next value from the iterator object
# The iteration tool keeps calling the __next__() method until it raises a StopIteration exception
# The StopIteration exception is raised when there are no more values to return from the iterator object
# The iteration tool then stops the iteration and the loop ends


# >>> myLists = [1,2,3,4]
# >>> I = iter(myLists)
# >>> I
# <list_iterator object at 0x76efa7dff070>

# This above code shows that the iter() function returns a reference to the iterator object in memory.


# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x76efa7dff070>

# After we call the __next__() method the reference to the iterator object in memory remains the same. Because the reference is provided for the start of the iterator object.


# Files by default are iterable objects. So we can use the iter() function to get a reference to the iterator object in memory. However list or any other iterable objects are not iterable objects by default. So we need to use the iter() function to get a reference to the iterator object in memory.

# f = open('chai.py')
# >>> iter(f) is f
# True
# >>> myNewList = [1,2,3,4]
# >>> iter(myNewList) is myNewList
# False
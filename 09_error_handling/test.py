file = open('youtube.txt', 'w')

# If you do not do it in try catch then it will try to find a file and if not found, it will create new file.

try:
    file.write('Sreedev')
finally:
    file.close()


# Newer way of opening file in Python

# This will take care of file open and close automatically
with open('youtube.txt', 'w') as file:
    file.write('Sreedev')

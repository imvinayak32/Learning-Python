import math
# Built-in functions for numbers
gpa = 8.632

print(abs(gpa))  #absolute function, returns positive value
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1)) #round off by nearest 1 decimal number, here wrt 6
print(round(gpa, 2)) # wrt 3

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")

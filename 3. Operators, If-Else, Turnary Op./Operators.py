x = 48
y = 10

# Basic Operators =>
print(x + y)
print(x - y)
print(x*y)
print(x/y) # division with remainder
print(x//y) # round off to nearest lower integer
print(round(x/y)) # round off to nearer larger integer
print(x%y) # gives remainder

# Here also we have +=, -=, *=, /=
# /= return answer with floating point

# Some Other Operators -
#  >, <, <=, >=, not, and, or

meaning = 42
print('')
print('')
print('')
print('')
 
if meaning > 10:
    print('Greator than 10')
else:
    print('less than 10')

# Ternary Operator
print('Right on!') if meaning < 10 else print('Not today')

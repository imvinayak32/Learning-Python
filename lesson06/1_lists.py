# Different type of list:

users = ['Dave', 'John', 'Sara'] #same data
data = ['Dave', 42, True] # different data can be here
emptylist = [] #it could empty
furniture = ['table', 'chair', 'rack', 'shelf']

print("Dave" in emptylist)


# Accessing the List
print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2]) # 2 is not included
print(users[1:]) # from 1 till end
print(users[-3:-1]) # -1 is not included
print(furniture[:])


# Length of list
print(len(data))



users = ['vin']
data = ['Dave', 42, True]

# List Methods :

users.append('Elsa')
print(users)

users += ['Jason'] #added in the end
print(users)

# users.extend(['Robert', 'Jimmy']) #added in the end
# print(users)

# users.extend(data) # two list can be mereged into one
# print(users)

users.insert(0, 'Bob')
print(users)

users.insert(2,'harsh')
print(users)

users.insert(1,'oggg')
print(users)

# users[2:2] = ['Eddie', 'Alex']
# print(users)

# users[1:3] = ['Robert', 'JPJ']
# print(users)

# users.remove('Bob')
# print(users)

# print(users.pop())
# print(users)

# del users[0]
# print(users)

# # del data
# data.clear()
# print(data)

# users[1:2] = ['dave']
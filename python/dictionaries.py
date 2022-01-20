# Key:Value pair
# Key is always unique

d1 = {1: 'A', 'B': 2, 4.5: 45, 'Hello': 'Hi'}
# print(d1)

# print(d1['B'])
# print(d1['Hello'])

d1['Hello'] = 'Hola'  # Existing value is updated
# print(d1)

d1['Bye'] = 'Bye Bye'  # Key was not there, so new key:value is added
print(d1)

# del d1['Bye']  # Completely removes the element
# print(d1)

# removed = d1.pop('B') #To store the removed value
# print(d1)
# print(removed)

for values in d1:
    print(values)

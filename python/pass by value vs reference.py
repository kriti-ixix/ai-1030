l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l1  # Passing by reference

print(l1 == l2)  # To compare the values
print(l1 is l2)  # To compare the memory addresses
print(l1 is l3)

l1[0] = 10
print(l3)

l3[4] = 50
print(l1)

l3 = l1.copy()  # Passing by value
l3[4] = 100
print("l3:", l3)
print("l1:", l1)
s1 = {1, 2, 4, 6, 8}
s2 = {2, 5, 10, 6, 30}

'''Intersection
Common elements between two sets'''
print("Intersection:")
print(s1 & s2)
print(s1.intersection(s2))

'''Union
Combines the two sets'''
print("Union")
print(s1 | s2)
print(s1.union(s2))

'''Set difference
Elements of A but not in B'''
print("Difference")
print(s1 - s2)
print(s1.difference(s2))

'''Symmetric Difference
Elimanates the common elements and keep the
unique elements from both sets'''
print("Symmetric Difference")
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

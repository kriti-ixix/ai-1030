# squares = {}

l1 = list(range(1, 11))
print(l1)

l2 = list(range(10, 110, 10))
print(l2)

# {1:1, 2:4, 3:6, 4:16, 5:25, 6:36}

# for key in l1:
#     squares[key] = key ** 2

squares = {key:key ** 2 for key in l1}
print(squares)

for (x, y) in zip(l1, l2):
    print("Key:", x, "Value:", y)

d = {x:y for (x, y) in zip(l1, l2)}
print(d)
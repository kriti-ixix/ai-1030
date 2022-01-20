l1 = list(range(1, 11))
print(l1)

# squares = []

# for i in l1:
#     squares.append(i**2)

squares = [number**2 for number in l1]  # List comprehension

even_squares = [number**2 for number in l1 if number % 2 == 0]

l2 = [number**2 if number % 2 == 0 else number for number in l1]

print(squares)
print(even_squares)
print(l2)
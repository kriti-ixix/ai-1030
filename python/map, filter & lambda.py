l1 = list(range(1, 11))
print(l1)


def times10(x):
    return x * 10


# l2 = [times10(number) for number in l1]
# print(l2)
# This can be reduced to

l2 = list(map(times10, l1))
print(l2)

# Now in map, no loop is used, only map object is used

l1 = list(range(1, 11))
print(l1)

l2 = list(map(lambda x: x*10, l1))
print(l2)
# By using lambda expression there is no need to write small functions

# Only for Boolean Values
l1 = list(range(1, 11))
print(l1)


# def checkEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


l2 = list(filter(lambda num: num % 2 == 0, l1))
print(l2)

# Filter only stores true value and discards false value

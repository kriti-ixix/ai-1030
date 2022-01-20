#Function definition

'''
Types of functions:
- On the basis of parameters
    1. Default method
    2. Parameterised function
- On the basis of return type
    1. No return type
    2. Some return type
'''

def addition():
    x = 5
    y = 10
    print(x + y)

def subtraction(a, b):
    print(a - b)

def multiplication(a, b=1, c=1):
    d = a * b * c 
    return d

addition()
subtraction(10, 20)
p1 = multiplication(10, 20, 30)
p2 = multiplication(100, 200, 300)
p3 = multiplication(10)

print("The products are", p1, p2, p3)
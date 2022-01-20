def sum(a, b):
    return (a+b)


def sub(a, b):
    return (a-b)


def mul(a, b):
    return (a*b)


def div(a, b):
    return (a/b)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Please choose the operation you want to perform ")
print("1. Sum")
print("2. Sub")
print("3. Mul")
print("4. Div")

selection = int(input())

if(selection == 1):
    answer = sum(x, y)
elif(selection == 2):
    answer = sub(x, y)
elif(selection == 3):
    answer = mul(x, y)
elif(selection == 4):
    answer = div(x, y)

print("The answer is", answer)
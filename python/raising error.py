try:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))

    if length < 0 or breadth < 0:
        raise ValueError

    area = length * breadth
    print("Area is", area)

except ValueError:
    print("Length or breadth cannot be negative")

except:
    print("Error")
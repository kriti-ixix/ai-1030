shoes = {38:4, 39:0, 40:5, 37:3, 41:10}

while True:
    size = int(input("Enter the size you want: "))

    if size == 0:
        print("Thank you!")
        break

    if shoes[size] == 0:
        print("Out of stock")
    else:
        shoes[size] -= 1
        print("Here's your shoe!")
        #shoes[size] = shoes[size] - 1
        print(shoes)

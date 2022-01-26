try:
    num = int(input("Enter a number: "))    
    print(num)
    l1 = [1, 2, 3, 4]
    print(l1[num])

# except ValueError:
#     print("This number is invalid")

# except IndexError:
#     print("The index does not exist")

except Exception as e:
    print(e)

finally:
    print("End of program")

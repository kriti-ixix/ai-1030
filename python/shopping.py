filename = 'Shopping List.txt'
items = {'Eggs':1, 'Chocolate':2}
choice = input("Do you want to add or view the list? ")

if choice == 'view':
    pass

elif choice == 'add':
    f = open(filename, 'w')
    item = input("What do you want to add? ").capitalize()

    if item in items.keys():
        items[item] += 1
    else:
        items[item] = 1

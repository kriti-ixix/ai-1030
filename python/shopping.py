filename = 'Shopping List.txt'
items = {}
choice = input("Do you want to add or view the list? ")

if choice == 'view':
    f = open(filename, 'r')
    content = f.read()
    print(content)
    f.close()

elif choice == 'add':
    f = open(filename, 'r')

    existing_list = f.read().split("\n")
    existing_list.pop()
    print(existing_list)

    f.close()

    # f = open(filename, 'w')
    # item = input("What do you want to add? ").capitalize()

    # if item in items.keys():
    #     items[item] += 1
    # else:
    #     items[item] = 1

    # for item, qty in items.items():
    #     f.write(f"{qty} {item}\n")

    # f.close()
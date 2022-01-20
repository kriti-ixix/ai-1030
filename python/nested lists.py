def view():
    print(f"The list of Students:\n{li}\n")


def add():
    name = input("Enter the name you want to add: ")
    li.append(name)
    print(f"Added {name} on index {(len(li)-1)}")
    print(f"New list: \n{li}\n")


def remove():
    x = int(input("Enter the index number of student you want to delete: "))
    print(f"Removed {li.pop(x)}")
    print(f"New list: \n{li}\n")


def update():
    x = int(input("Enter the index you want to update: "))
    name = input("Enter the new entry: ")
    li[x] = name
    print(f"New list:\n{li}\n")


num = int(input("Enter the number of students: "))
li = []

for i in range(num):
    student = input(f"Enter {i} student name: ")
    li.append(student)

while True:
    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. Update")
    print("5. Exit")
    opt = int(input("Enter your choice: "))

    if(opt == 1):
        view()
    elif(opt == 2):
        add()
    elif(opt == 3):
        remove()
    elif(opt == 4):
        update()
    elif(opt == 5):
        break

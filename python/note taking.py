filename = input("Enter file name: ") + ".txt"

print("Enter your choice: ")
choice = input("-Read -Write -Append: ").lower()

if choice == 'read':
    f = open(filename, 'r')
    notes = f.read()
    print(notes)
    f.close()

elif choice == 'write':
    f = open(filename, 'w')
    num = int(input("Enter number of notes: "))

    for i in range(1, num + 1):
        note = input(f"Enter note {i}: ")
        f.write(f"Note {i}: {note}\n")

    f.close()

elif choice == 'append':
    f = open(filename, 'r')
    note_counter = 0

    for line in f:
        note_counter += 1

    note_counter += 1
    f.close()

    f = open(filename, 'a')
    num = int(input("Enter number of notes: "))

    for i in range(note_counter, note_counter + num):
        note = input(f"Enter note {i}: ")
        f.write(f"Note {i}: {note}\n")

    f.close()

else:
    print("Invalid option")
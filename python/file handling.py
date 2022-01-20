cities = ['Los Angeles', 'New York', 'Paris', 'Mumbai', 'Delhi', 'Rome']

file = open('Cities.txt', 'w')

for city in cities:
    file.write(city + '\n')  # Write should contain only string as input
print("File saved!")
file.close()

file = open('Cities.txt', 'r')

content = file.read() #Read all the file in one go and displays
print(content)

for line in file:
    print(line)  # Reads content line by line

file.close()

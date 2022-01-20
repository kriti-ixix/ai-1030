myList = ["XYZ", "ABC", 1, 10.5, True, "Hello"]
print(myList)

#Indexing
print(myList[3])
print(myList[-1]) #Negative Indexing

#Overwriting
myList[2] = 20
print(myList)

#Slicing
#el[start=0 : stop = len : step=1]
print(myList[1:5])
print(myList[1:5:2])
print(myList[::-1])

#Extra functions
myList.append(10)
print(myList)

myList.insert(1, "How are you?")
print(myList)

removedItem = myList.pop() # Last element removed by default
print(removedItem)

myList.pop(2)

#Iterating over a list
for i in myList:
    print(i)
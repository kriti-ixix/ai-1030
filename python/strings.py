s1 = "Hello world!"

# Indexing
print(s1[0])
print(s1[8])
print(s1[-1])  # last element
print(s1[-2])  # second last element

# Slicing [start : stop : step]
print(s1[::-1])

print(len(s1))
print(s1.upper())
print(s1.lower())
print(s1.capitalize())

# String formatting
name = "ABC"
rollno = 5
marks = 45.5
output = f"Roll No {rollno} {name} got {marks} marks"
print(output)

# String split
message = "Hi! How are you?"
tweet = "Good morning! #Rainy #Cold #Thandi"

splitMessage = message.split()
print(splitMessage)
splitTweet = tweet.split('#')
print(splitTweet)
hashtags = tweet.split('#', 2)
print(hashtags)

for c in message[::-1]:
    print(c, end="")
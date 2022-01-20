# Sets: Unordered and only store unique values

s1 = {'a', 1, 5, 5, 5, 5, 5, True, True, 'a', "Hello", "Hello"}
print(s1)

s1.add(20) # Will be added
s1.add(5) # Will be ignored

countries = []
countriesSet = set()  # Declaration of empty set

for i in range(5):
    countries.append(input("Please enter your country: "))

countriesSet = set(countries)
print(countries)
print(countriesSet)

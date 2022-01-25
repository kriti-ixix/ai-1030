import re

# a-z A-Z 0-9 @ a-z . com/org \w
# ^ - start with that pattern
# + - 1 or more occurences
# \w - any combination of words
# {m, n} - occurence between m and n
# $ - end with this pattern 

regex = '^[a-z0-9]+[@]\w+[.]\w{2,3}$'

email1 = "kriti22@gmail.com"
email2 = "abcd"
email3 = "@hi"

print(re.search(regex, email1))
print(re.search(regex, email2))
print(re.search(regex, email3))
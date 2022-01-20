l1 = [1, 45, 36, 100, 80, 95, 74]
print(l1)
num = int(input("Enter the number you want to find index of: "))
# temp = 0

# for number in l1:
#     if number == num:
#         print("Number found at index")
#         temp += 1

# for i in range(0, len(l1)):
#     if l1[i] == num:
#         print("Number found at index", i)
#         temp += 1

# if temp == 0:
#     print("Number not found")

if num in l1:
    print(f"{num} found at index {l1.index(num)}")
else:
    print(f"{num} not found")

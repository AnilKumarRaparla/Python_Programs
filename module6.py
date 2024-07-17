str1 = input("Super string: ")
str2 = input("Substring: ")
flag = 0
l = str1.split()
for i in l:
    if i == str1:
        flag = 1
        break
print(i)
if i == l:
     print(str1,":Found")
else:
     print("Not found")
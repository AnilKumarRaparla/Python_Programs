str = "srinarhreddy"
unique = set(str)
for char in unique:
    count = str.count(char)
    print(char, '-', count)
cnt=0
for char in str:
    cnt=cnt+1
print("Total count:",cnt)
str1=input("String 1:")
str2=input("String 2:")
if (str1==str2):
    print("Equal")
else:
    print("Not Equal")

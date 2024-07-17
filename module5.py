string = "anilkumar"
print("Given input is: ",string)
output = ""
for char in string:
    if char not in output:
        count = string.count(char)
        output += char + "-" + str(count) + "\n"
print(output)
    #string equal or not
string2 = "anilkumar"
if string == string2:
    print("Equal")
else:
    print("Not Equal")
    #Total count
cnt=0
for char in string:
    cnt=cnt+1
print("Total count:",cnt)
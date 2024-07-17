s = input("Enter a string:")
ch = input("Desired char:")
res = ""
for i in s:
    if i.isalpha():
        res = res + i
        ch = i
    else:
        res = res + chr(ord(ch)+int(i))
print("Output is :",res)
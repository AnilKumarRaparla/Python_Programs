str = input().strip()
char = input().strip()
if len(str) < 2:
    print("-1")
else:
    if str[0] == str[-1]:
        count = str.count(char)
        print(count)
    else:
        print("0")

def reverseWords(s):
    '''sailu'''
    arr = s.split(" ")
    sb = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != "":
            sb.append(arr[i])
            sb.append(" ")
    return "".join(sb).strip() if len(sb) > 0 else ""
s = input()
res=reverseWords(s)
print(res)
print(reverseWords.__doc__)

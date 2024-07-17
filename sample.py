#To print lenght of the without len() method:
s = input()
l1 = s.split()
l2 = []
i = len(l1)-1
while(i>=0):
    l1.append(l1[i])
    i = i-1
    res = ' '.join(l1)
print(res)

n = int(input())   
arr1 = list(map(int, input().split()))   
arr2 = list(map(int, input().split()))
res = []
for i in range(n):
    res.append(arr1[i])
    res.append(arr2[i])
print(' '.join(map(str, res)))

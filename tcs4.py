n = int(input()) 
arr = list(map(int, input().split()))  
arr.sort()  
res=[]
for i in range(0, n-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(" ".join(str(x) for x in arr))

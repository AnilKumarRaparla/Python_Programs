def fun(lst,target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if(lst[i]+lst[j]==target):
                return [i,j]
    return []
lst = list(map(int, input("Enter: ").split()))
target = int(input("Enter the target: "))

print(fun(lst, target))



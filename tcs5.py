def function(arr, m):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)): 
            print(arr[i],arr[j])
            if (arr[i] + arr[j]) % m == 0:
                count += 1
    return count
arr = [10, 9, 4, 5, 7, 2, 8, 20, 21]
m = 15
print(function(arr, m))  

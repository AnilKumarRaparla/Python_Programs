def fun(arr, target):
    arr.sort()  
    left = 0
    right = len(arr) - 1
    
    closest_sum = float('inf')
    closest_pair = None
    
    while left < right:
        pair_sum = arr[left] + arr[right]
        
        if abs(pair_sum - target) < abs(closest_sum - target):
            closest_sum = pair_sum
            closest_pair = arr[left], arr[right]
        
        if pair_sum == target:
            return closest_pair
        elif pair_sum < target:
            left += 1
        else:
            right -= 1
    
    return closest_pair
arr = [3, 4, 2, 3, 5]
target = 4
result = fun(arr, target)
print(*result)

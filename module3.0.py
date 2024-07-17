n = int(input()) 
L = list(map(int, input().split()))
R = list(map(int, input().split()))
max_value = -1
max_ind = -1
for i in range(n):
    value = L[i] * R[i]
    if value > max_value:
        max_value = value
        max_ind = i
    elif value == max_value:
        if R[i] > R[max_ind]:
            max_value = value
            max_ind = i
print(max_ind + 1)

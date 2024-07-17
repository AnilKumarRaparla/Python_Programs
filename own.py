A = "abcd"
B = "anilkumar"
count = 0
for char in B:
    print(char)
    if char in A:
        A = char + A.replace(char, '', 1)
        count += 1
        print(A)
print(count)

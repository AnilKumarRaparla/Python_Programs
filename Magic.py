def isMagicNumber(num):
    sum = 0
    temp = num
    while temp > 0:
        sum += temp % 10
        temp //= 10
    return (sum * (num // sum)) == num
number = int(input("Enter a number"))
if isMagicNumber(number):
    print(number, "is a magic number")
else:
    print(number, "is not a magic number")
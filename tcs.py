def funtion(n):
    if n % 2 == 0:
        print("Even series:",3 ** (n // 2 - 1))
    else:
        print("Odd series:",2 ** (n // 2))
n = int(input())
funtion(n)
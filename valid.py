
num = [2]
num2 = [15]
if num > num2:
    print("Provide valid number")
else:
    for i in range(num, num2+1):
        flag = 0
        for j in range(2,i):
            if(i%j==0):
                flaf = 1
                break
            if(flag==0):
                print(i,end="")
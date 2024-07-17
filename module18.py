string = input("Enter combination of digits,alpha and spec:")
sorted_str = ''.join(sorted(string))
print(sorted_str)
dgts=""    
for i in sorted_str:
        if i.isdigit():
            dgts += i
print("Given digits are:",dgts)
sum = 0
for digit in str(dgts): 
      sum += int(digit)      
print("Sum is: ",sum)
if sum!=1:
    for i in range(sum):
        if sum % 2 == 0:
            print("NO")
            break
        else:
            print("YES")
            break


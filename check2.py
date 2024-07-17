def palindrome(str1):
    return str1 == str1[::-1]

input1 = "geeksoskeeg"
output1 = palindrome(input1)
if output1:
    print("Yes")
else:
    print("No")

input2 = "geeksforgeeks"
if palindrome(input2):
    print("Yes") 
else:
   print("No") 


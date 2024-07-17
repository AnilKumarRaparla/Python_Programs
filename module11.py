#Python program to check whether the string is Symmetrical or Palindrome
def check_palindrome(input_string):
    if input_string == input_string[::-1]:
        return True
    else:
        return False

def check_symmetrical(input_string):
    mid = len(input_string)//2
    if len(input_string) % 2 == 0:
        if input_string[:mid] == input_string[mid:][::-1]:
            return True
        else:
            return False
    else:
        if input_string[:mid] == input_string[mid+1:][::-1]:
            return True
        else:
            return False

input_string = input("Enter a string: ")
if check_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
if check_symmetrical(input_string):
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")


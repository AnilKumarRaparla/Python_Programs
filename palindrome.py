def is_palindrome(num):
    return str(num) == str(num)[::-1]
def next_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num
input_num = int(input("Enter a number:"))
next_palindrome_num = next_palindrome(input_num)
print(f"The next palindrome number after: {input_num} is  {next_palindrome_num}")


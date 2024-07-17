\
    """Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama. """


def isPalindrome(s: str) -> bool:
    # convert to lowercase and remove the non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


def isPalindromeType2(s: str) -> bool:
    alpha = []
    for char in s:
        if char.isalnum():
            alpha.append(char.lower())
    return alpha == alpha[::-1]

str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"
str3 = " "


print(isPalindrome(str1))  # Output: True
print(isPalindrome(str2))  # Output: False
print(isPalindrome(str3))  # Output: True
print(isPalindromeType2(str1)) #output: True


"""s = "A man, a plan, a canal: Panama"
alphanumeric_chars = []
for char in s:
    if char.isalnum():
        alphanumeric_chars.append(char.lower())
if alphanumeric_chars == alphanumeric_chars[::-1]:
    print("true")
else:
    print("false")"""

def reverseVowels(s: str) -> str:
    # Convert the string to a list of characters
    s_list = list(s)
    # Initialize left and right pointers
    left, right = 0, len(s) - 1
    # Define set of vowels
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    # Loop until left pointer meets or passes the right pointer
    while left < right:
        # If left character is not a vowel, move the left pointer
        if s_list[left] not in vowels:
            left += 1
        # If right character is not a vowel, move the right pointer
        elif s_list[right] not in vowels:
            right -= 1
        # If both characters are vowels, swap them and move the pointers
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    # Convert the list of characters back to a string and return
    return ''.join(s_list)

s = "hello"
print(reverseVowels(s))  # Output: "holle"

s = "leetcode"
print(reverseVowels(s))  # Output: "leotcede"



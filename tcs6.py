def remove_chars(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(remove_chars(str1, str2))
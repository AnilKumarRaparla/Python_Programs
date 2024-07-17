#Python – Avoid Spaces in string length:
input_string = input("Enter a string: ")
length = len(input_string.replace(' ', ''))
print("Length of the string (without spaces):", length)

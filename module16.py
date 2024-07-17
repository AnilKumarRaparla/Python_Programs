def uppercase_latter_part(string):
    midpoint = len(string) // 2
    first_half = string[:midpoint]
    second_half = string[midpoint:]
    second_half = second_half.upper()
    result = first_half + second_half
    return result

# Accept input from user
string = input("Enter a string: ")

# Call function to perform uppercase of latter part of the string
result = uppercase_latter_part(string)

# Print the result
print(result)


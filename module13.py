#Ways to remove i’th character from string in Python:
def remove_character(input_string, i):
    new_string = ''
    for index, character in enumerate(input_string):
        if index != i:
            new_string += character
    return new_string

input_string = input("Enter a string: ")
i = int(input("Enter the index of the character to be removed: "))
print("New string:", remove_character(input_string, i))

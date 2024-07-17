#Reverse words in a given String in Python:
def reverse_words(input_string):
    words = input_string.split()
    reverse_words = [word[::-1] for word in words]
    return ' '.join(reverse_words)

input_string = input("Enter a string: ")
print("Reversed words:", reverse_words(input_string))


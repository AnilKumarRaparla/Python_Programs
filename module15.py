vowels = set('aeiou')
string = input("Enter a string: ")
# Convert input to lowercase and remove any spaces
string = string.lower().replace(" ", "")
# Check if all vowels are present in the string
if vowels.issubset(set(string)):
    print("String contains all vowels")
else:
    print("String does not contain all vowels")

#program to convert first and last letters to uppercase in words of string?
def convert_low_to_upp(string):
    words = string.split()
    result = []  
    for word in words:
        first_letter = word[0].upper()
        last_letter = word[-1].upper()
        middle = word[1:-1]
        result.append(first_letter + middle + last_letter) 
    return ' '.join(result)
#count_vowels
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0 
    for char in string:
        if char in vowels:
            count = count + 1   
    return count
#find_uncommon_words
def find_uncommon_words(string):
    # split the string into words
    words = string.split()
    unique_words = set(words)
    common_words = set()
    for word in words:
        if word in unique_words:
            unique_words.remove(word)
        else:
            common_words.add(word)          
    return list(unique_words - common_words)
string = input("Enter a String:")
print(convert_low_to_upp(string)) 
print(count_vowels(string))
print(find_uncommon_words(string))

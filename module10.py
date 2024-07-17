def find_uncommon_words(string):
    # split the string into words
    words = string.split()
    unique_words = set(words)
    common_words = set()
    # iterate over the words and add common words to a set
    for word in words:
        if word in unique_words:
            unique_words.remove(word)
        else:
            common_words.add(word)
            
    # return the difference between the unique words and the common words
    return list(unique_words - common_words)
string = 'pace ace'
print(find_uncommon_words(string))  # output
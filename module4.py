def count_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts
input_str = "ppppbbbaace"
output = count_chars(input_str)
print(output) 

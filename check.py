vowels = set('aeiou')
ccount = 0
vcount = 0
input1 = "aeioup??"
for char in input1:
    if char.isalpha():
        if char.lower() in vowels:
            vcount += 1
            ccount = 0
        else:
            ccount += 1
            vcount = 0
        
        if vcount > 5 or ccount > 3:
            output1 = 0
            break
else:
    output1 = 1

print(output1)  # Output: 1

# Example 2
input2 = "bcdaeiou??"
for char in input2:
    if char.isalpha():
        if char.lower() in vowels:
            vcount += 1
            ccount = 0
        else:
            ccount += 1
            vcount = 0
        
        if vcount > 5 or ccount > 3:
            output2 = 0
            break
else:
    output2 = 1

print(output2)  # Output: 0

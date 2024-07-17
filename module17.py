string = input("Enter a string:")
vowels = 'aeiouAEIOU'
print("given input is:",string)
string_list = list(string)
for i in range(len(string_list)-1):
    if string_list[i] in vowels and string_list[i+1] in vowels:
        string_list[i], string_list[i+1] = string_list[i+1], string_list[i] 
new_string = ''.join(string_list)
print(new_string)
 
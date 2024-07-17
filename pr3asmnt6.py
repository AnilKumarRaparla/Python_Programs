#Anagarm
def Fun(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)
str1 = input("Enter a string:") 
str2 = input("Enter a string:")
print(Fun(str1,str2))
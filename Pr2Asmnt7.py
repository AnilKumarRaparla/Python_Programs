def SubstringPattern(s: str) -> bool:
    return s in (s + s)[1:-1]
s = input("Enter a String:")
print(SubstringPattern(s))

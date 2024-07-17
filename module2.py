str = "Go123sir@#$"
alph=""
digi=""
spec=""
for i in str:
   if i not in i.isalpha() or i.isdigit():
       spec = spec +i
print(spec)

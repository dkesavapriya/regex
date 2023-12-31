import re
text=input("Enter the input:")
match=re.search("[0-9]$",text)
print(match)
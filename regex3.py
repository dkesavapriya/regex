import re
text=input("Enter the input:")
match=re.search("O?k{2,3}",text)
print(match)
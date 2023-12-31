import re
text=input("Enter the input:")
match=re.search("N?o*",text)
print(match)
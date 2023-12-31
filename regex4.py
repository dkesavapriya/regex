import re
text=input("Enter the input:")
match=re.search("^[a-z|A-Z]",text)
print(match)
# main.py created inside day 95
#  regular expression--> Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# Metacharacters in regular expressions:-
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs

import re
pattern= r"[a-z]+ing"
text="Regular expressions are a powerful tool for working with strings and text data in Python. Whether you're matching patterns, replacing text, or extracting, information, regular expressions make it easy to perform complex string operations with just a few lines of code. With a little bit of practice, you'll be able to use regular expressions to solve all sorts of string-related problems in Python."

#Searching for a pattern in re using re.search() Method
# match=re.search(pattern, text)
#Searching for a pattern in re using re.findall() Method
# match=re.findall(pattern,text) #Returns a list of strings
#Replacing a pattern
match=re.sub(pattern,'dog (glti se bola)', text)
print(match)

pattern= r"[a-z]+ing"
matches=re.finditer(pattern,text)  #Returns iterator of match objects
for i in matches:
    print(i)
    
    #imporatnt link-https://docs.python.org/3/library/re.html
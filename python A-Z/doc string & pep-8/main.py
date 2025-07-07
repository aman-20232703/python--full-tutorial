# main.py created inside day 29
# doc-string(string litrals that appear right after the defination of a function,method,class or method) & PEP-8
def square(n):
    '''take a nunmber n, return the square of n'''  # always come right after function,method,class & just above body
    print(n**2)
square(5)
print(square.__doc__)  # accessing docstring using this doc attribute
#by changing comments we can't change output of programme but it is possible in doc-string

# PEP-8(python enhancement proposal) is type of guidelines which provided best practice on how to write python code
"""The Zen of Python, by Tim Peters:-
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
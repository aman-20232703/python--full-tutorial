# main.py created inside day 41
#41 shorthand if-else # maximize readability
a=7
b=44
c=9 if a>b else 0          #(result=value_if_true if condition else value_if_false)
print(c)
print(a) if a>b else print("=") if a==b else print(b)

c=9 if a>b else 0
print(c)

a=22
b=44
if a>b:
    print(a)
else:
    print(b)
result=print(a) if a>b else print(b) # shorthand of above code

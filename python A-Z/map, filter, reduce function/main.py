# main.py created inside day 53
#   map & filter & reduce- these are higher order function because they take function as a argunment in a another function, syntax- map(function,iterable)

def cube(x):
    return x*x*x
print(cube(2))

# but if we have more than one number for calculation
#1st method using for loop
x=[1,2,3,4,5]
new=[]
for i in x:
    new.append(cube(i))
print(new)

#2nd metod using map
#map
x=[1,2,3,4,5]
new=list(map(cube,x))  # we can use lambda function in place of cube also
print(new)

#filter(qualify element from the list)
def filter_function(a):
    return a>2

new=list(filter(filter_function,x))
print(new)


#reduce(take first two element as a argunment and perform operation and give finalresult)
from functools import reduce
# def sum(x,y):
#     return x+y
number=[1,2,3,4,5]
add=reduce(lambda x,y: x+y,number)
print(add)
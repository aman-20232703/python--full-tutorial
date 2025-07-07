# main.py created inside day 25
# methods in tuple
n=("aman","raj","aditya","sahil")
p=list(n)  #if we try to change tuple then first convert it into list
print(p)
p.append("vikash")
print(p)
p.pop(2)
print(p)
n=tuple(p)   # after doing changing in tuples convert again it into list
print(n)

#methods in tuple
n=(2,3,6,7,2,8,3,9)
print(n.count(2))
print(n.index(8))

l=(2,4,3,5,2,6,7)
print(l.index(2,4,7))  # return index of 2 lie between 4-7 which is 4

print(len(n))

m=(2,6,4,8)
x=m+n    # can concatenate
print(x)
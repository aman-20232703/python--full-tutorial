# main.py created inside day 54
# is Vs ==(is compare exact location of object in memory & == compare value of two objets)
a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)  # compare exact location/identity of object in memory
print(a==b)   # compare value

a=3  # it is a constant value which are always immutable
b=3  # it is also a constant value which are always immutable
print(a is b)
print(a==b)

a=(1,5)  # it is a tuple  which are always immutable
b=(1,5)  # it is also tuple which are always immutable
print(a is b)
print(a==b)

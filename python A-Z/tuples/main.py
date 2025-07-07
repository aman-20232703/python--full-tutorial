# main.py created inside day 24
#24. tuples(similar to list but only difference is that it is immutable, denoted by(....))
tup=(1,2,3,4,5,6)    # tup=[22,4,34,"aman",True]  # can store different datatypes,# length and index are different things e.g- here length of list is 6 and index is 5

print(tup,type(tup))    #tup= (1), print(type(tup))- then type of tup will be int not tuple so we write it tup=(1,)

print(len(tup))
print(tup[4])
print(tup[:5])     # after slicing there will be return new tuple
print(tup[len(tup)-4:5])

if 4 in tup:
    print("yes")
else:
    print("no")
    
tup=(i for i in range(10) if i%2!=0)
print(tup)
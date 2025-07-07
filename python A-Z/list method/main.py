# main.py created inside day 23
# 
#23. methods in list
l=[2,3,4,5,1,6]
# l.append(55)   # add no. at the last
# l.insert(4,100) # add no. at particular index
# l.extend([33,56,48])   # add range of no. at the end of list

# print(l.sort() )#ascending order
# print(l.sort(reverse=True) )#descending order
# print(l.reverse())  # reverse the original list

print(l.index(5))   # return the index of first occurance of list item

l=[2,4,3,5,2,6,7]
print(l.index(2,4,7))  # return index of 2 lie between 4-7 which is 4

print(l.count(5))    # count number of 5
print(l.copy())     # we know list is mutable but we can copy it and then make changes in the list

k=[22,88,34,78]
m=l+k
print(m)   # concatenate two list
print(l)




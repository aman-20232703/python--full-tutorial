# main.py created inside day 32
#methods in set
s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

states={"bihar","up","jharkhand","mp","rajsthan","haryana"}
states2={"maharastra","karnataka","tamilnadu","bihar","mp"}
# states3=states.union(states2)
# print(states,states2,states3)

# states3=(states.intersection(states2))
# states.intersection_update(states2)
# print(states)

print(states.symmetric_difference(states2))  # not common
print(states.symmetric_difference_update(states2))

print(states.difference(states2)) # delete common
print(states.isdisjoint(states2))  #intersection zero
print(states.issuperset(states2))  # all the elements of states2 lie within states
print(states2.issubset(states))  #vice-versa
print(states.add("mp"))           # add new value
print(states.update(states))    # update
# states.remove("bihar")
states.discard("bihar")  # same work as remove but it does not throw error when item is absent
print(states)
print(states2.pop())  # delete random value anywhere from set
del states2       # it is not a method , it delete set entirly
print(states2)

z={1,2,3,4,6,7}
print(z.clear())  #this method clear all the items
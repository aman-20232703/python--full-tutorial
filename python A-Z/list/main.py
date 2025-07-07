# main.py created inside day 22
# list(seperated by comaas and square barcket, store multiple data in same variable, mutable, can have ordered collection of diffrent data types, denoted by [...])
# marks=[22,4,34,"aman",True]  # can store different datatypes
marks=[22,4,34,56,23,67]   # length and index are different things e.g- here length of list is 6 and index is 5
print(marks)
print(type(marks))
print(marks[4])
print(marks[-3])  #print(marks[len(marks)-3])=3 index  ,print(marks[6-3]) ,print(marks[3])
print(marks[2]==45) # change index 2 no. 34 --> 45, lists are mutable

if 4 in marks:
    print("yes")
else:
    print("no")
    
if "ma" in "aman":
    print("yes")
else:
    print("no")
    
print(marks[:]) # [o:len(marks)] python automatically use this & after slicing there will be changes in original list
print(marks[1:])
print(marks[1:6:2])      #for i in range(1,6,2) use in this way in for loop

#list comprehension
list=[i for i in range(20) if i%2==0]
print(list)
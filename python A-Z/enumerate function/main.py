# main.py created inside day 42
# enumerate function(a built-in function in python that allow to loop over a sequence and get the index and value of each element
marks = [12,13,44,56,28,99,23]
index=0
for mark in marks:
    print(mark)
    if(index==5):
        print("great! aman")
    index+=1

#2nd method of above by using enumerate
marks = [12,13,44,56,28,99,23]
for index,mark in enumerate(marks): # for index,mark in enumerate(marks, start=1): - if we want to start index from 1 instead of 0
    print(index,mark)
    if(index==3):
        print("great! aman")

    
#printing reverse of a number
count=524342
n=0
while(count>0):
    a=count%10
    count=count//10
    n=n*10+a

print(n)
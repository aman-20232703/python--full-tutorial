# main.py created inside day 19
#break statement enable a programme to skip over a part of code, it also terminate the loop.
for i in range(12):   # we can also use it with while loop in same way
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1))
print("outside of loop")

# continue terminate the iteration and jump into the next iteration
for i in range(12):
    if(i==10):
        continue
    print("5*",i+1,"=",5*(i+1))
print("loop terminated")

# main.py created inside day 14
# else-if
a=int(input("enter your age: "))

if(a>18):
    print("ready")
else:
    print("not ready")

#elif
a=int(input("enter your age: "))
if(a>18):
    print("yes")
elif(a<18):
    print("no")
else:
    print("none")
print("thankyou")
    
#nested-if
a=int(input("enter your age: "))

if(a<18):
    print("no")
elif(a>18):
    if(a==20):
        print("yes")
    elif(a<30):
        print("none")
    else:
        print("ok")
print("thankyou")
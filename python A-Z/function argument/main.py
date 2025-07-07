# main.py created inside day 21
#  function argumnets(default,keyword,variable,required)
#default
def sum(a=4,b=5):
    print("sum is: ",a+b)
sum()                        # by default add a+b perform from above function

#keyword
def sum(a=3,b=5):
    print("sum is: ",a+b)
sum(b=3,a=22)                 #position not matter in parenthesis

#required
def sum(a,b=5):
    print("sum is: ",a+b)
sum(3)                         #required a value to run the function like here value of a required

#variable
def avg(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("avg is: ",sum/len(numbers))
avg(1,2,3,4,5,6,7,8,9,10)                  #variables as a tuple

def name(**name):
    print("hello," , name["fname"], name["mname"], name["lname"] )
name(mname="kumar", lname="singh", fname="aman")                 #variables as a dict

#return
def sum(a,b):
    return a+b
c=sum(2,5)   # c value store result of return
print("sum is:",c)

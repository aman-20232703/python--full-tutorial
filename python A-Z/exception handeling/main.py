# main.py created inside day 36
#  excepion handling[try:except](process of responding to unitended and unexpected error/ events when a computer programme runs,it help to mainatain flow of code)
# from logging import exception
n=input("enter value: ")
print(f"multiplication table of {n} is: ")
try:
    for i in range (1,11):
        print(f"{int(n)}X{i}={int(n)}*{i}")
except:                        # we can also write- Except exception as e:
    print("invalid input:")
    
print("imp. line of codes")
print("last...")

try:
    p=int(input("enter value number: "))
    a=[3,8]
    print(a[p])
except ValueError:
    print("number is not integer.")
except IndexError:
    print("index number error")
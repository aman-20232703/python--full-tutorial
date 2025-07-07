# main.py created inside day 16
# match case
x =int(input("enter the value: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:                    # default case
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)

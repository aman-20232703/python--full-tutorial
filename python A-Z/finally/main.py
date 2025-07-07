# main.py created inside day 37
# finally clause(it is always excecuted in exception handeling so it is generally used for doing conclusion task like closing the resources and closing the databases connection or may be ending tech programme)
try:
    a=[1,4,7,3,9,5]
    l=int(input("enter the index: "))
    print(a[l])
except:
    print("some error Occured")
finally:
    print("i am always Excecuted")
# print("i am always Excecuted")     # we can also print above statement without finally but it cannot use within function but still we need finally because there may be possibility to occur error and i wnt to revoke database connection , file cleanup and closing any file.

def function():
    try:
        a=[1,4,7,3,9,5]
        l=int(input("enter the index: "))
        print(a[l])
        return 1
    except:
        print("some error Occured")
        return 0
    finally:
        print("i am always Excecuted")
x=function()
print(x)
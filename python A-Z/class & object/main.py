# main.py created inside day 57
# class and object in python
class person:                   #creating a class
    name="aman"
    occupation="software developer"
    networth= 10000000
    
    def info(self):
        print(f"{self.name} has good income of networth {self.networth}")  # creating a method which is a instance method( here self means the object for that method is calling, it is compulsory to define self if we are creating any method within class)
    
a=person()                   # creating a object
b=person()                   # creating another object
c=person()
print(a.name,a.networth)

a.name="aman kumar"
a.networth=2000000
print(a.name,a.networth)
a.info()                       #calling method

a.name="suraj shahu"
a.networth=3000000
print(f"{a.name}   {a.networth}")
a.info()                        #calling method
c.info()   # here if i will not assign/change any value to the c then it get default values
# main.py created inside day 65
#  static method(it is method that belong to a class rather than an instance of a classes, no need to write self in this method)

class math:
    def __init__(self,num):
        self.num=num
        
    def addname(self,n):
        self.num=self.num+n
        
    @staticmethod    #static method
    def add(a,b):
        return a+b
a=math(2)
print(a.num)

a.addname(3)
print(a.num)

print(a.add(4,5))   # calling instance method
print(math.add(4,5)) # calling method using class


# class method as a alternative constructor
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
a=employee("aman", 20000)
print(a.name)
print(a.salary)

string="love-3026098"
b=employee.fromstr(string)
print(b.name)
print(b.salary)
# main.py created inside day 72
# super keyword --> The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

#When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.
#e.g 1
class ParentClass:
    def parent_method(self):
        print("This is the parent method 1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("aman")
        super().parent_method()
        
    def child_method(self):
        print("This is the child method 2.")

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

#e.g 2
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        
a= employee('aman kumar',2345)
b= programmer('akash',456, 'python')
print(a.name,a.id)
print(b.name,b.id,b.lang)

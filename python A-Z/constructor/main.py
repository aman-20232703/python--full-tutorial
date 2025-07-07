# main.py created inside day 58
# constructor, syntax- def __init__(self) (it is a special method in a class used to create and initialize an object of a class. there are different types of constructor.it invoked automatically when an object of a class is created)
class person:
    def __init__(self,na,oc):  #creating a constructor
        self.name=na        #here name is the property of that object & na is simple, temporary variable which passed as a argunment and local variable for init function
        self.occ=oc
        
    def info(self):   #creating a method(it is a instance method and it always refers to instance variable)
        print(f"{self.name} is a {self.occ}")
        
a=person("aman kumar", "software developer")  # here we are taking only two argunment instead of 3 because object 'a' paased in self argunment automatically so we ignore it
b=person("jyoti singh", "HR")
a.info()
b.info()
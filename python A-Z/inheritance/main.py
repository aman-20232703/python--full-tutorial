# main.py created inside day 61
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdetails(self):
        print(f"the name of the employee: {self.id} is {self.name}")
        
class programmer(employee):        # inherited new programmer class from the employee class
    def showlanguages(self):
        print("he is a pyhton programmer")
        
a=employee("aman kumar", 324)
a.showdetails()

b=programmer("AMAN KUMAR", 363)
b.showlanguages()
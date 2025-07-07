# main.py created inside day 69
# class method
class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
        
    @classmethod    # whenever i use class method decorator then it will get first argument as a class not as a instance so that we can directly change class, we can change variable of class(by default it get first element as a instance)
    def changecompany(cls, newcompany):    # non need to write self here because it assume first argunment as a object
        cls.company=newcompany
        
a=employee()
a.name="aman"
a.show()

a.changecompany("microsoft")
a.show()

print(a.company)
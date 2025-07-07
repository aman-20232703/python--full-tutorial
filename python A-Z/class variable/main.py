# class variables--(Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class.) Vs instance variables-- (Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class)

class employee:
    company='Google'         # class variable
    def __init__(self,name):
        self.name=name    # instance variable
        self.amount=0.02  # instance variable
        
    def deatils(self):
        print(f"the person working in the {self.company} is {self.name} whose amount is {self.amount}")
        
a=employee('aman')
a.amount=200
a.company='Microsoft'  # if instance variable available then it use it (company=microsoft)
a.deatils()

b=employee('kumar')   # if instance variable not available for this then we search for the class variable (company=google)
b.deatils()
# main.py created inside day 79
# multiple inheritence(Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.)
#e.g- 1
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
        
a=Animal('dog', 'dogie')
print(a.name,a.species)
a.make_sound()

b=Dog('dog','doges','red')
print(b.name,b.breed,b.fur_color)  # MULTIPLE INHERITENCE(ATTRIBUTES)
b.make_sound()

#e.g- 2
class employee:
    def __init__(self,name):
        self.name=name
    
    def shown(self):
        print(f"the name is {self.name}")
        
class developer:
    def __init__(self,developer):
        self.developer=developer
        
    def shows(self):
        print(f"the developer is {self.developer}")
        
class employeedeveloper(employee,developer):
    def __init__(self,name,developer):
        self.name=name
        self.developer=developer
        
    def show(self):
        print("all right!")
        
a=employee('aman')
b=developer('python')
print(a.name,b.developer)
a.shown()
b.shows()

c=employeedeveloper("aman","python")
print(c.name,c.developer)
c.show()
c.shown()  # MULTIPLE INHERITENCE(METHOD)
c.shows()

print(employeedeveloper.mro())  # track the method of your classes function(The .mro() function returns a list of classes that Python will search through in order when trying to resolve methods or attributes — especially important in inheritance, particularly multiple inheritance.)
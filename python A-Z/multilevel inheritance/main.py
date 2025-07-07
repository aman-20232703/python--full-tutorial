# main.py created inside day 80
#  multilevel inheritence(Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.)
# syntax{
#     class BaseClass:
#     # Base class code
    
# class DerivedClass1(BaseClass):
#     # Derived class 1 code
    
# class DerivedClass2(DerivedClass1):
#     # Derived class 2 code
# }

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
        
a= Animal('dog','dogie')
print(a.name, a.species)
a.show_details()
print("\n")

b=Dog('dog','breed')
print(b.name,b.breed)
b.show_details()
print("\n")

c=GoldenRetriever('dog','black')
print(c.name,c.color)
c.show_details()

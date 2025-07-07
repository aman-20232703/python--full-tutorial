# main.py created inside day 81
#81. Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

# In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.
# syntax:-
# class baseclass:
#     pass

# class derived1(baseclass):
#     pass

# class derived2(baseclass):
#     pass

# class deridev3(derived1, derived2):
#     pass

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address
        
    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)
        
class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration
        
    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)
        
class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program
        
    def show_details(self):
        Person.show_details(self)
        self.program.show_details()
    
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()

# Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.
#syntax-
# class baseclass:
#     pass

# class derived1(baseclass):
#     pass

# class derived2(baseclass):
#     pass

# class deridev3(derived1):
#     pass

class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)
        
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
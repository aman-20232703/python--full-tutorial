# main.py created inside day 78
# single inheritance(Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.)
#e.g- 1
# Parent class
class Animal:
    def speak(self):
        print("Animals can make sounds.")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Create object of child class
d = Dog()

# Call methods
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog

#e.g- 2
class animal:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        
    def live(self):
        print(f"{self.name} is living in {self.location}")
    
class cat(animal):
    def __init__(self,name,location,breed):
        super().__init__(name,location)
        self.breed=breed
        
    def live(self):
        print(f"{self.name} is living in {self.location}")
        
    
b=animal('cat','home')
print(b.name,b.location)
b.live()

b=cat('cat','home','catie')
print(b.name,b.location,b.breed)

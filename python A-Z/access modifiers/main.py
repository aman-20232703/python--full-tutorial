# main.py created inside day 62
"""
access modifiers in oops(Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.) but in python there is no concepts of access modifiers like other programming language but still we do it for our convenience.

Types of access specifiers:-
1. Public access modifier-(All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.)"""
# class Student:
#     # constructor is defined
#     def __init__(self):
#         self.name = 'aman'             # public variable

# obj = Student()
# print(obj.name)

"""2. Private access modifier(By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.)"""
# class student:
#     def __init__(self):
#         self.__name = "aman"            # An indication of private variable(by using mangling or doublr underscore)

# obj = student()
# # print(obj.__name)   # Throws an AttributeError(private)
# print(obj._student__name)  # but we can still accsess this private variable here and successfully printed

"""# Protected access modifier(In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.
# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.)"""

# class student:
#     def __init__(self):
#         self._name = "aman"            # protected method using single _

# obj = student()
# print(obj._name)
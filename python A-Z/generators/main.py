# main.py created inside day 91
#  Generators--> Generator are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

# Creating a Generator--> In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. Here's an example:

def my_generator():
    for i in range(1,8):
        yield i
        
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# also we can use it using for loop
for i in gen:
    print(i)
    
# As you can see, the generator function my_generator() returns a generator object, which can be used to generate the values in the range 1 to 4. The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function

# Benefits of Generators-->Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

# Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.

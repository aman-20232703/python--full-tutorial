# main.py created inside day 86
# walrus  --> The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
#The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.
#e.g- 1(using usual method)
numbers=[1,2,3,4,5]
while True:
    if len(numbers)>0:
        print(numbers.pop())
        
# using walrus method
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

#e.g-2(using usual method)
foods=list()
while True:
    food=input('your food is: ')
    if food=='quit':
        break
    foods.append(food)
print(foods)

#using walrus method
foods=list()
while(food := input('your food is: ')) != 'quit':   #using walrus operator(:=j)
    foods.append(food)
print(foods)
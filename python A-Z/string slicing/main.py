# main.py created inside day 12
#string slicing -- A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array. Note: This method of specifying the start and end index to specify a part of a string is called slicing.
fruits="mango"
print(len(fruits))   # We can find the length of a string using len() function.
print(fruits[1:4])
print(fruits[:5])
print(fruits[0:-3])  # print(fruits[0:len(fruits)-3])
print(fruits[-3:-1])

na="harry"
print(na[-4:-2])
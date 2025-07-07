"""
#3. Modules and pip in Python!--> Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

# Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
# External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

# The pip command-- It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command. e.g-- pip install pandas

# Using a module in Python (Usage)--> We use the import syntax to import a module in Python. Here is an example code:
import pandas
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file

"""
"""
# we cannot install built-in module using pip e.g- shutil
python module:---
1                   _weakref            htmlmin             rlcompleter
PIL                 _weakrefset         http                runpy
__future__          _winapi             idlelib             sched
__hello__           _wmi                idna                scipy
__phello__          _xxinterpchannels   imagehash           seaborn
_abc                _xxsubinterpreters  imaplib             secrets
_aix_support        _yaml               imghdr              select
_ast                _zoneinfo           importlib           selectors
_asyncio            abc                 inspect             shelve
_bisect             aifc                io                  shlex
_blake2             annotated_types     ipaddress           shutil
_bz2                antigravity         itertools           signal
_codecs             argparse            jinja2              site
_codecs_cn          array               joblib              six
_codecs_hk          ast                 json                smtplib
_codecs_iso2022     asyncio             keyword             sndhdr
_codecs_jp          atexit              kiwisolver          socket
_codecs_kr          attr                lib2to3             socketserver
_codecs_tw          attrs               linecache           sqlite3
_collections        audioop             locale              sre_compile
_collections_abc    base64              logging             sre_constants
_compat_pickle      bdb                 lzma                sre_parse
_compression        binascii            mailbox             ssl
_contextvars        bisect              mailcap             stackL
_csv                builtins            markupsafe          stat
_ctypes             bz2                 marshal             statistics
_ctypes_test        cProfile            math                string
_datetime           calendar            matplotlib          stringprep
_decimal            certifi             mimetypes           struct
_elementtree        cgi                 missingno           subprocess
_functools          cgitb               mmap                sunau
_hashlib            charset_normalizer  modulefinder        symtable
_heapq              chunk               msilib              sys
_imp                cmath               msvcrt              sysconfig
_io                 cmd                 multimethod         tabnanny
_json               code                multiprocessing     tangled_up_in_unicode
_locale             codecs              my code             tarfile
_lsprof             codeop              name                telnetlib
_lzma               collections         netrc               tempfile
_markupbase         colorama            networkx            test
_md5                colorsys            nntplib             textwrap
_msi                compileall          nt                  this
_multibytecodec     concurrent          ntpath              threading
_multiprocessing    configparser        nturl2path          time
_opcode             contextlib          numbers             timeit
_operator           contextvars         numpy               tkinter
_osx_support        contourpy           opcode              token
_overlapped         copy                operator            tokenize
_pickle             copyreg             optparse            tomllib
_py_abc             crypt               os                  tqdm
_pydatetime         csv                 packaging           trace
_pydecimal          ctypes              pandas              traceback
_pyio               curses              pandas_profiling    tracemalloc
_pylong             cycler              pathlib             tty
_queue              dataclasses         pdb                 turtle
_random             datetime            phik                turtledemo
_sha1               dateutil            pickle              types
_sha2               dbm                 pickletools         typing
_sha3               decimal             pip                 typing_extensions
_signal             difflib             pipes               tzdata
_sitebuiltins       dis                 pkgutil             unicodedata
_socket             doctest             platform            unittest
_sqlite3            email               plistlib            urllib
_sre                encodings           poplib              urllib3
_ssl                ensurepip           posixpath           uu
_stat               enum                pprint              uuid
_statistics         errno               profile             venv
_string             faulthandler        pstats              visions
_strptime           filecmp             pty                 warnings
_struct             fileinput           py_compile          wave
_symtable           fnmatch             pyclbr              weakref
_testbuffer         fontTools           pydantic            webbrowser
_testcapi           fractions           pydantic_core       winreg
_testclinic         ftplib              pydoc               winsound
_testconsole        functools           pydoc_data          wsgiref
_testimportmultiple gc                  pyexpat             xdrlib
_testinternalcapi   genericpath         pylab               xml
_testmultiphase     getopt              pyparsing           xmlrpc
_testsinglephase    getpass             python              xxsubtype
_thread             gettext             pytz                yaml
_threading_local    glob                pywt                zipapp
_tkinter            graphlib            queue               zipfile
_tokenize           gzip                quopri              zipimport
_tracemalloc        hashlib             random              zlib
_typing             heapq               re                  zoneinfo
_uuid               hmac                reprlib
_warnings           html                requests"""


"""
#4. Write a program to print hello python
print("hello pyhon")

#5. Python Comments
#A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.
#Single-Line Comments: To write a comment just add a ‘#’ at the start of the line.
#Multi-Line Comments: To write multi-line comments you can use ‘#’ at each line or you can use the multiline string(''' '''/ """ """).

# Escape Sequence Characters:- To insert characters that cannot be directly used in a string, we use an escape sequence character.An escape sequence character is a backslash \ followed by the character you want to insert. An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

print("This doesnt "execute")
print("This will \" execute")

# Other Parameters of Print Statement
# object(s): Any object, and as many as you like. Will be converted to string before printed
# sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# end='end': Specify what to print at the end. Default is '\n' (line feed)
# file: An object with a write method. Default is sys.stdout
print(object(s), sep=separator, end=end, file=file, flush=flush)

#6. variable-- Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Harry"
d = None
These are four variables of different data types.

Data Type-- Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. In python, we can print the type of any operator using type function:

a = 1
print(type(a))
b = "1"
print(type(b))


By default, python provides the following built-in data types:

1. Numeric data: int, float, complex
int: 3, -8, 0
float: 7.349, -9.0, 0.0000001
complex: 6 + 2i

2. Text data: str
str: "Hello World!!!", "Python Programming"

3. Boolean data:consists of values True or False.

4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
Output: [8, 2.3, [-4, 5], ['apple', 'banana']]

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

Example:
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
Output: (('parrot', 'sparrow'), ('Lion', 'Tiger'))

5. Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}

#7. Operators
Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

Arithmetic operators
Operator	Operator Name	Example
+	Addition	       15+7=12
-	Subtraction	       15-7=8
*	Multiplication	   5*7=35
**	Exponential	       5**3=125
/	Division	       5/3=1.6
%	Modulus	           15%7=2
//	Floor Division	   15//7=3

"""







"""
#8. Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!

a = int(input("enter 1st number: ", ))
b = int(input("enter 2nd number: ", ))

print("required results:- ")

#for addition
adddition=a+b
print("1.adddition of",a,"and",b,"is",adddition)

#for subtraction
subtraction=a-b
print("2.subtraction of",a,"and",b,"is",subtraction)

#for multiplication
multiplication=a*b
print("3.multiplication of",a,"and",b,"is",multiplication)

#for division
division=a/b
print("4.division of",a,"and",b,"is",division)

print("thankyou :)")
"""


"""
#9. typcasting-- The conversion of one data type into the other data type is known as type casting in python or type conversion in python. Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# Two Types of Typecasting: 1.Explicit Conversion (Explicit type casting in python), 2.Implicit Conversion (Implicit type casting in python).

#Explicit typecasting: The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion. It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

string ="12"
number= 2

string_number=int(string)
add1=number+string_number
print("addition is:",add1)  # explicit typecasting
print("type of this variable",type(add1))

# add=string+number
# print("addition",add)

#  Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

b=2.9
c=3
d=b+c
print("addition is:",d)  # implicit typecasting(python intrpreter automatically convert it according to requirement)
print("type of this variable",type(d))

"""

"""
#10. taking user input in python-- In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
a = input("enter number: ")
b = input("enter number: ")
print(a+b)             # it assume all the variable as string
print(int(a)+int(b))   # there we need to initialize datatype of our variable- "int"

"""


"""
#11. STRING- What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters. SINGLE AND MULTI LINE STRING

#12. string slicing -- A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array. Note: This method of specifying the start and end index to specify a part of a string is called slicing.
fruits="mango"
print(len(fruits))   # We can find the length of a string using len() function.
print(fruits[1:4])
print(fruits[:5])
print(fruits[0:-3])  # print(fruits[0:len(fruits)-3])
print(fruits[-3:-1])

na="harry"
print(na[-4:-2])
"""


"""
#13 string method(strings are immutable , when we perform operations it can't change string, it only make copy of last strings)
a ="!!aMAn kUmAr is gooD bOy00!!!!!"                #collable=()
print(a.lower())
print(a.upper())
print(a.rstrip("!"))          # remove exclamation from last
print(a.replace("aMAn","aman"))  # change all occurances of aMAn to aman
print(a.split(" "))           # convert string into list
print(a.capitalize())         #capitalize first character of string into upper case
print(len(a))
print(len(a.center(8)))       # add 8 length between centre of string means total (31+8=39)
print(a.count("aMAn"))
print(a.endswith("kUmAr"))    # give boolean value that it ends with kUmAr or not
print(a.endswith("mA",9,11))  # give boolean value that it ends with mA as well as given its range or not
print(a.startswith("aMAn"))   # give boolean value that it start with aMAn or not
print(a.find("is"))           # return - index 1st occurance or -ve for missing occurance
print(a.index("A"))           # sure to return , not return - sign

d="ramanujan college"
print(d.isalnum()) # ALPHABETICAL + NUMBER available or not
print(d.isalpha()) # ALPHABETICAL available or not
print(d.islower()) # given letters are in lowercase or not
print(d.isupper()) # given letters are in uppercase or not

b ="aMAn kUmAr is GooD bOy00"
print(b.isprintable())   # is pritable or not
print(b.isspace())   # " "=whitespace available or not
print(b.istitle())   # all latters are in titlle case or not
print(a.title())     # convert leeters to title case

c="aman kumar"
print(c.swapcase())  # toggle between capital and small letters

"""


# conditional statements
"""
#14. else-if
a=int(input("enter your age: "))

if(a>18):
    print("ready")
else:
    print("not ready")

#elif
a=int(input("enter your age: "))
if(a>18):
    print("yes")
elif(a<18):
    print("no")
else:
    print("none")
print("thankyou")
    
#nested-if
a=int(input("enter your age: "))

if(a<18):
    print("no")
elif(a>18):
    if(a==20):
        print("yes")
    elif(a<30):
        print("none")
    else:
        print("ok")
print("thankyou")


#15. time module
import time
tm=time.strftime("%H:%M:%S")  #strftime is a function which give us hour and minute
print(tm)
tm=time.strftime("%H")
print(tm)
tm=time.strftime("%M")
print(tm)
tm=time.strftime("%S")
print(tm)


import time
tm=int(time.strftime("%H"))
if (tm<12):
    print("good morning")
elif(tm<14 and tm>11):
    print("good afternoon")
elif(tm>14):
    if(tm<18):
        print("good evening")
    else:
        print("goodnight")
else:
    print("not match")


#16. match case
x =int(input("enter the value: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:                    # default case
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)

#. loops
#17. for loops(iterate over a sequence of iterable or objects) repeating
k="aman kumar"
for i in k:
    print(i)

list=["aman","putu","suraj","vikash"]
for i in list:
    print(i)

for i in range(5):
    print(i)

for i in range(3,8):
    print(i)

for i in range (1,100,7):
    print(i)


#18. while loops(print only condition satisfied)
# count=0
# while(count<=5):
#     print(count)
#     count+=1
# else:
#     print("finish")

t=5
while(t>=0):
    print(t)
    t-=1

#else with while loop
count=0
while(ount>0):
    print(count)
    count-=1
else:
    print("all done")
    
#do while loop- executed atleast once
while true:  #using infinite loop
    x=int(input("enter number: "))
    print(x)
    if x>0:
        break

#19. break statement enable a programme to skip over a part of code, it also terminate the loop.
for i in range(12):   # we can also use it with while loop in same way
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1))
print("outside of loop")

# continue terminate the iteration and jump into the next iteration
for i in range(12):
    if(i==10):
        continue
    print("5*",i+1,"=",5*(i+1))
print("loop terminated")



#20. function is a block of code that perform specific task whether it is called, is help reduce same line code uses at diffrent palce by calling function
def gmean(a,b):
    a=(a*b)/(a+b)
    print(a)
    
def greatervalue(a,b):
    if(b>a):
        print("b greater")
    else:
        print("not grater")
        
a=3
b=5
gmean(a,b)
greatervalue(3,5)

def calculator(a,b):
    pass               # this is used when we want to use any function after sometime
    
#two types of function- 1. built-in function(predefined like min(), max(), dict(), list() etc.), 2. user defined function(user need to def...)

#21. function argumnets(default,keyword,variable,required)
#default
def sum(a=4,b=5):
    print("sum is: ",a+b)
sum()                        # by default add a+b perform from above function

#keyword
def sum(a=3,b=5):
    print("sum is: ",a+b)
sum(b=3,a=22)                 #position not matter in parenthesis

#required
def sum(a,b=5):
    print("sum is: ",a+b)
sum(3)                         #required a value to run the function like here value of a required

#variable
def avg(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("avg is: ",sum/len(numbers))
avg(1,2,3,4,5,6,7,8,9,10)                  #variables as a tuple

def name(**name):
    print("hello," , name["fname"], name["mname"], name["lname"] )
name(mname="kumar", lname="singh", fname="aman")                 #variables as a dict

#return
def sum(a,b):
    return a+b
c=sum(2,5)   # c value store result of return
print("sum is:",c)


#22. list(seperated by comaas and square barcket, store multiple data in same variable, mutable, can have ordered collection of diffrent data types, denoted by [...])
# marks=[22,4,34,"aman",True]  # can store different datatypes
marks=[22,4,34,56,23,67]   # length and index are different things e.g- here length of list is 6 and index is 5
print(marks)
print(type(marks))
print(marks[4])
print(marks[-3])  #print(marks[len(marks)-3])=3 index  ,print(marks[6-3]) ,print(marks[3])
print(marks[2]=45) # change index 2 no. 34 --> 45, lists are mutable

if 4 in marks:
    print("yes")
else:
    print("no")
    
if "ma" in "aman":
    print("yes")
else:
    print("no")
    
print(marks[:]) # [o:len(marks)] python automatically use this & after slicing there will be changes in original list
print(marks[1:])
print(marks[1:6:2])      #for i in range(1,6,2) use in this way in for loop

#list comprehension
list=[i for i in range(20) if i%2==0]
print(list)


#23. methods in list
l=[2,3,4,5,1,6]
# l.append(55)   # add no. at the last
# l.insert(4,100) # add no. at particular index
# l.extend([33,56,48])   # add range of no. at the end of list

# print(l.sort() )#ascending order
# print(l.sort(reverse=True) )#descending order
# print(l.reverse())  # reverse the original list

print(l.index(5))   # return the index of first occurance of list item

l=[2,4,3,5,2,6,7]
print(l.index(2,4,7))  # return index of 2 lie between 4-7 which is 4

print(l.count(5))    # count number of 5
print(l.copy())     # we know list is mutable but we can copy it and then make changes in the list

k=[22,88,34,78]
m=l+k
print(m)   # concatenate two list
print(l)


#24. tuples(similar to list but only difference is that it is immutable, denoted by(....))
tup=(1,2,3,4,5,6)    # tup=[22,4,34,"aman",True]  # can store different datatypes,# length and index are different things e.g- here length of list is 6 and index is 5

print(tup,type(tup))    #tup= (1), print(type(tup))- then type of tup will be int not tuple so we write it tup=(1,)

print(len(tup))
print(tup[4])
print(tup[:5])     # after slicing there will be return new tuple
print(tup[len(tup)-4:5])

if 4 in tup:
    print("yes")
else:
    print("no")
    
tup=(i for i in range(10) if i%2!=0)
print(tup)


#25. methods in tuple
n=("aman","raj","aditya","sahil")
p=list(n)  #if we try to change tuple then first convert it into list
print(p)
p.append("vikash")
print(p)
p.pop(2)
print(p)
n=tuple(p)   # after doing changing in tuples convert again it into list
print(n)

#methods in tuple
n=(2,3,6,7,2,8,3,9)
print(n.count(2))
print(n.index(8))

l=(2,4,3,5,2,6,7)
print(l.index(2,4,7)  # return index of 2 lie between 4-7 which is 4

print(len(n))

m=(2,6,4,8)
x=m+n    # can concatenate
print(x)


#26. import time
hour=int(input("enter your timing-: "))
# a=int(input("select standard time zone: "))
if(hour>0 and hour<12):
    print("good morning")
elif(hour>11 and hour<17 ):
    print("good afternoon")
elif(hour>17 and hour<24):
    print("good evening")

#27. ~ create a programme capable of displaying question to the user like KBC.
~ use list data type to store the questions and their correct answers.
~ display the final amount the person is taking home after playing the game.

28. #f-string(we can put variables within string)
letter="my name is {0} and i am from {1}"   #using indexing
name="aman kumar"
country="India"
print(letter.format(name,country))              # (country,name)reverse the order of name and country
print(f"my name is {name} iam from {country}")  # using f-string

# we can retain our f-string as it is by-- print(f"my name is {{name}} iam from {{country}}")

txt="for only {price:.2f} dollars!"  #using 2 decimal places
price=49.99999
print(txt.format(price=49.99999))
print(f"for only {price:.2f} dollars!")    # using f-string

#29. doc-string(string litrals that appear right after the defination of a function,method,class or method) & PEP-8
def square(n):
    '''take a nunmber n, return the square of n'''  # always come right after function,method,class & just above body
    print(n**2)
square(5)
print(square.__doc__)  # accessing docstring using this doc attribute
#by changing comments we can't change output of programme but it is possible in doc-string

# PEP-8(python enhancement proposal) is type of guidelines which provided best practice on how to write python code
The Zen of Python, by Tim Peters:-
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

#30. recursion(recursion is the process of defining something in terms of itself or function calling within function)
def factorial(n):
    if (n==0 or n==1):      #base value
        return 1
    else:
        return n*factorial(n-1)   #recursive value
print(factorial(5))
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (n-1)+(n-2)
print(fibonacci(5))


#31. set is a collection of well defined object, it store unordered, multiple and unique items in {} bracket, unchangable, contain different datatypes,
s={1,2,3,4,2,5,4,7,8,9,5}
print(s)
print(type(s))   # set will not take repeated value

a={}
print(type(a))  #it gives empty dict...
b=set()
print(type(b))  # it gives empty set

q={"Aman",3,77,"Kumar","@",0,12}
for i in q:
    print(i)   # unordered
    
#32. methods in set
s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

states={"bihar","up","jharkhand","mp","rajsthan","haryana"}
states2={"maharastra","karnataka","tamilnadu","bihar","mp"}
# states3=states.union(states2)
# print(states,states2,states3)

# states3=(states.intersection(states2))
# states.intersection_update(states2)
# print(states)

print(states.symmetric_difference(states2))  # not common
print(states.symmetric_difference_update(states2))

print(states.difference(states2)) # delete common
print(states.isdisjoint(states2))  #intersection zero
print(states.issuperset(states2))  # all the elements of states2 lie within states
print(states2.issubset(states))  #vice-versa
print(states.add("mp"))           # add new value
print(states.update(states))    # update
# states.remove("bihar")
states.discard("bihar")  # same work as remove but it does not throw error when item is absent
print(states)
print(states2.pop())  # delete random value anywhere from set
del states2       # it is not a method , it delete set entirly
print(states2)

z={1,2,3,4,6,7}
print(z.clear())  #this method clear all the items

#33. dictionaries(store key value items in key : value pairs tha are seperated by , and denoted {}, unordered but according to python 3.7 dict is ordered)
dict={
    2703:"aman",
    2708:"brijesh",
    2731:"rupesh",
    2741:"suraj",
    2745:"vikash",
    2778:"sahil"
}
print(dict)
print(dict[2703])   #output:- aman

info={"name":"aman", "age":20, "course":"B.voc"}
print(info)
print(info["name"])
# print(info["name2"]) #if not exist throw error
print(info.get("name2")) #if not exist print none
print(info.get("name")) #if exist print
print(info["age"])

print(info.keys())  #printing all keys

for key in info.keys(): #1st method for printing values
    print(info[key])
print(info.values()) #2nd method for printing values

print(info.items())  #accessing '(key , value)' of dict....

for key,value in info.items():
    print("the value corresponding to the {key} is {value}")
    
#34. methods in dict...
ep1={2703:"aman",2708:"brijesh",2731:"rupesh",2741:"suraj",2745:"vikash",2778:"sahil"}
ep2={2749:"ashutosh",2729:"ritik"}

ep1.update(ep2)  # combine ep1 & ep2
# ep1.clear()   # print empty dict.(ep1={})
# ep1.pop(2741)  # remove particular key ,value pair.
# del ep1[2741]   # remove particular key ,value pair.
# ep1.popitem()  # remove last value of dict.
print(ep1)

#35. for-else loop
for i in range(9):
    print(i)
else:                # loop khtm hogya so execute else
    print("sorry no i")

for i in range(9):
    print(i)
    if i==4:
        break
else:                 # loop break ho gya hai so not execute else
    print("sorry no i")

#36. excepion handling[try:except](process of responding to unitended and unexpected error/ events when a computer programme runs,it help to mainatain flow of code)
# from logging import exception
n=input("enter value: ")
print(f"multiplication table of {n} is: ")
try:
    for i in range (1,11):
        print(f"{int(n)}X{i}={int(n)}*{i}")
except:                        # we can also write- Except exception as e:
    print("invalid input:")
    
print("imp. line of codes")
print("last...")

try:
    p=int(input("enter value number: "))
    a=[3,8]
    print(a[p])
except ValueError:
    print("number is not integer.")
except IndexError:
    print("index number error")
    
#37. finally clause(it is always excecuted in exception handeling so it is generally used for doing conclusion task like closing the resources and closing the databases connection or may be ending tech programme)
try:
    a=[1,4,7,3,9,5]
    l=int(input("enter the index: "))
    print(a[l])
except:
    print("some error Occured")
finally:
    print("i am always Excecuted")
# print("i am always Excecuted")     # we can also print above statement without finally but it cannot use within function but still we need finally because there may be possibility to occur error and i wnt to revoke database connection , file cleanup and closing any file.

def function():
    try:
        a=[1,4,7,3,9,5]
        l=int(input("enter the index: "))
        print(a[l])
        return 1
    except:
        print("some error Occured")
        return 0
    finally:
        print("i am always Excecuted")
x=function()
print(x)


#38. raise custom error(we can create our own error to check evry steps of code & debugging  )
a=(input("enter any value between 2 and 9 or string 'quit': "))
if a=="quit":
    raise ValueError("only this string is acceptable")
elif(int(a)<2 or int(a)>9):
    raise ValueError("value not in range")
else:
    print("ohh! great,value in range")

#39 kaun banega crorepati
#40 secret code
#41 shorthand if-else # maximize readability
a=7
b=44
c=9 if a>b else 0          #(result=value_if_true if condition else value_if_false)
print(c)
print(a) if a>b else print("=") if a==b else print(b)

c=9 if a>b else 0
print(c)

a=22
b=44
if a>b:
    print(a)
else:
    print(b)
result=print(a) if a>b else print(b) # shorthand of above code


#42 enumerate function(a built-in function in python that allow to loop over a sequence and get the index and value of each element
marks = [12,13,44,56,28,99,23]
index=0
for mark in marks:
    print(mark)
    if(index==5):
        print("great! aman")
    index+=1

#2nd method of above by using enumerate
marks = [12,13,44,56,28,99,23]
for index,mark in enumerate(marks): # for index,mark in enumerate(marks, start=1): - if we want to start index from 1 instead of 0
    print(index,mark)
    if(index==3):
        print("great! aman")

    
#printing reverse of a number
count=524342
n=0
while(count>0):
    a=count%10
    count=count//10
        n=n*10+a

print(n)

#43. virtual environment
#44 import in python(process of loading code from python module into current script)
import math
#print(dir(math))  # give all functions of maths
# output: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
a=math.floor(4.36373)
print(a)
b=math.sqrt(9)
print(b)

from math import sqrt,pi   # we can import specific function from math module
r=sqrt(9)*pi
print(r)

#from math import *  # we can import everything of math function(not recomanded approach)
import math as m    #shorthand name of function or we can also expalin or elaborate
s=m.sqrt(36)
print(s)

from name import name,me  # import from other files, also we can write 'from name import *'
name()
print(me)

#45 if __name__ == "__main__"  (go and read name.py file)
import name
name.name()

#46 os module(built-in library that provide function for intrecting with operating system)
import os
os.mkdir(f"secret code")   # create folder secret code

for i in range(1,7):
    os.mkdir(f"secret code/code{i}")   # create 6 new folder code within secret code folder
    os.rename(f"secret code/code{i}",f"secret code/code {i}") # rename the folder

foldrs=os.listdir("secret code")     # show all folder in list
print(folders)

for folder in folders:
    print(folder)  # again show all folder but not in list
    print(os.listdir(f"secret code/{folder}")) # show all folder or file within secret code folder

os.remove("file or folder name")  # remove file or folder


#47 solution of secret codes


#48 local vs global varibles
# (local varibles is detected within a function and is only accessible within that function,it is created when the function is call and destroyed when function returns )
# (global varibles is a variable that defined outside of a function and its accessible from within any function from your code)

x=10              # global variable(outside function)
def my_function():
    y=4            #local variable(within function)
    print(y)
my_function()
print(x) # print global variable

x=10
def my_function():
    global x        # global keyword - this will change the value of global variable
    x=5
    y=4
    print(y)
my_function()
print(x)

#49. file handling(file modes), syntax-- (filename,mode), here mode is default not need to write
# https://www.geeksforgeeks.org/file-mode-in-python/
# ‘r’(read)	Open text file for reading. Raises an I/O error if the file does not exist.
f=open('myfile3.txt','r')
print(f)

# ‘r+’	Open the file for reading and writing. Raises an I/O error if the file does not exist.
text=f.read()
print(text)
f.close()

# ‘w’(write)	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
f=open('myfile.txt','w')
text1=f.write("hello ")
print(text1)
f.close()

# ‘w+’	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.

# ‘a’(append)	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
f=open('myfile.txt','a')
text1=f.write("hello ")
print(text1)
f.close()

with open('myfile.txt','a') as f:
    f.write("hello")   # by using this we need not to close file

# ‘a+’	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘rb’	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
# ‘rb+’	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
# ‘wb’	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘wb+’	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘ab’	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
# ‘ab+’	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.


#50 read and write line using readlines()-Python readlines() is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines.
#  writelines()-
f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
    print(line)
    
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in science is {m1}")
    print(f"marks of student {i} in english is {m2}")
    print(f"marks of student {i} in mathematics is {m3}")
    print(line)
    
f=open('myfile2.txt','w')
line=['line 1\n','line 2\n','line 3\n']
f.writelines(line)
f.close()



#51. seek() & tell()
with open('myfile3.txt','r') as f:
    print(type(f))
    
    f.seek(10) # allow you to move the current position within a file to specific position (move to the 10th byte in the file)
    data=f.read(8)
    print(data)
    
    print(f.tell())  # function return the current position within the file or tell which position we seek
    
with open('myfile3.txt','w') as f:
    f.write("hello world")
    f.truncate(4)    # help to read and write file after truncate

with open('myfile3.txt','r') as f:
    print(f.read())

    
#52. lambda function (use in a situation where a small function is required for a short period of time, they are commanly used as argument functions such as map, filter and reduce)
def double(x):
    print(2*x)   #return 2*x
double(3)       #print(double(3))

# 2nd method
double=lambda x: x*2
print(double(3))

avg=lambda x,y,z: (x+y+z)/3
print(avg(2,4,3))

def appl(fx,value):
    return 6+fx(value)
print(appl(lambda x: x*x*x, 2))      # print(appl(cube,2))- passing function within function


#53. map & filter & reduce- these are higher order function because they take function as a argunment in a another function, syntax- map(function,iterable)
def cube(x):
    return x*x*x
print(cube(2))

# but if we have more than one number for calculation
#1st method using for loop
x=[1,2,3,4,5]
new=[]
for i in x:
    new.append(cube(i))
print(new)

#2nd metod using mapx
#map
x=[1,2,3,4,5]
new=list(map(cube,x))  # we can use lambda function in place of cube also
print(new)

#filter(qualify element from the list)
def filter_function(a):
    return a>2

new=list(filter(filter_function,x))
print(new)


#reduce(take first two element as a argunment and perform operation and give finalresult)
from functools import reduce
# def sum(x,y):
#     return x+y
number=[1,2,3,4,5]
add=reduce(lambda x,y: x+y,number)
print(add)
    

#54. is Vs ==(is compare exact location of object in memory & == compare value of two objets)
a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)  # compare exact location/identity of object in memory
print(a==b)   # compare value

a=3  # it is a constant value which are always immutable
b=3  # it is also a constant value which are always immutable
print(a is b)
print(a==b)

a=(1,5)  # it is a tuple  which are always immutable
b=(1,5)  # it is also tuple which are always immutable
print(a is b)
print(a==b)


#55. SNAKE, PAPER, GUN
#56. OOPs in python
#57. class and object in python
class person:                   #creating a class
    name="aman"
    occupation="software developer"
    networth= 10000000
    
    def info(self):
        print(f"{self.name} has good income of networth {self.networth}")  # creating a method which is a instance method( here self means the object for that method is calling, it is compulsory to define self if we are creating any method within class)
    
a=person()                   # creating a object
b=person()                   # creating another object
c=person()
print(a.name,a.networth)

a.name="aman kumar"
a.networth=2000000
print(a.name,a.networth)
a.info()                       #calling method

a.name="suraj shahu"
a.networth=3000000
print(f"{a.name}   {a.networth}")
a.info()                        #calling method
c.info()   # here if i will not assign/change any value to the c then it get default values


#58. constructor, syntax- def __init__(self) (it is a special method in a class used to create and initialize an object of a class. there are different types of constructor.it invoked automatically when an object of a class is created)
class person:
    def __init__(self,na,oc):  #creating a constructor
        self.name=na        #here name is the property of that object & na is simple, temporary variable which passed as a argunment and local variable for init function
        self.occ=oc
        
    def info(self):   #creating a method(it is a instance method and it always refers to instance variable)
        print(f"{self.name} is a {self.occ}")
        
a=person("aman kumar", "software developer")  # here we are taking only two argunment instead of 3 because object 'a' paased in self argunment automatically so we ignore it
b=person("jyoti singh", "HR")
a.info()
b.info()
"""

#59. decoraters (it is function that takes another function as an argunment and return the new function that modifies the behaviour of the original function )
"""syntax-
@decorator_function
    def my_function():
        pass

def greet(fx):
    def mfx(*args,**kwargs):         # *args- take argunment as a tuple, **kwargs- take argunment as a dict..
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

def sum(a,b):
    print(a+b)
    
hello()  #we can also write 'greet(hello)()' then we no need to write @greet like above
greet(sum)(2,3)

#60. getter and setter
class myclass:
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print("value is {self._value}")
        
    @property                       #getter
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter               #setter
    def ten_value(self,new_value):
        self._value=new_value/10
        
a=myclass(10)
a.ten_value=67
print(a.ten_value)
a.show()

#61. inheritance 

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdetails(self):
        print(f"the name of the employee: {self.id} is {self.name}")
        
class programmer(employee):        # inherited new programmer class from the employee class
    def showlanguages(self):
        print("he is a pyhton programmer")
        
a=employee("aman kumar", 324)
a.showdetails()

b=programmer("AMAN KUMAR", 363)
b.showlanguages()

"""

"""#62. access modifiers in oops(Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.) but in python there is no concepts of access modifiers like other programming language but still we do it for our convenience.

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

"""
#63. S W G game
import random

def check(user, computer):
    if (computer==user):
        return 0
    if (computer==2 and user==0):
        return -1
    if (computer==1 and user==2):
        return -1
    if(computer==0 and user==1):
        return -1
    return 1
    
computer=random.randint(0,2)
user=int(input("enter your number: 0 for snake, 1 for water, 2 for gun: "))

print("user number", user)
print("computer number", computer)

score=check(user , computer)
if score==0:
    print("game draw")
elif score==1:
    print("you win")
else:
    print("you lose")
    
    

#64. library management system

#65. static method(it is method that belong to a class rather than an instance of a classes, no need to write self in this method)

class math:
    def __init__(self,num):
        self.num=num
        
    def addname(self,n):
        self.num=self.num+n
        
    @staticmethod    #static method
    def add(a,b):
        return a+b
a=math(2)
print(a.num)

a.addname(3)
print(a.num)

print(a.add(4,5))   # calling instance method
print(math.add(4,5)) # calling method using class



#66. class variables--(Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class.) Vs instance variables-- (Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class)

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

#67. library management system
class library:
    def __init__(self):
        self.nobooks=0
        self.books=[]
        
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
        
    def bookdetails(self):
        print(f"the library has {self.nobooks} books. these are : ")
        for i in self.books:
            print(i)
        
Library=library()
Library.addbook("book 1")
Library.addbook("book 2")
Library.addbook("book 3")
Library.addbook("book 4")
Library.bookdetails()
    

#68. clear and cutter
import os
folders=os.listdir("clutterfolder")
print(folders)
i=1
for folder in folders:
    os.rename(f"clutterfolder/{folder}",f"clutterfolder/{i}.jpg")
    i+=1


#69. class method
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



#70. class method as a alternative constructor
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
a=employee("aman", 20000)
print(a.name)
print(a.salary)

string="love-3026098"
b=employee.fromstr(string)
print(b.name)
print(b.salary)


#71. dir(), __dict__ and help() methods in python--> We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help().

# The dir() method--> The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
x=[3,5,3]
print(dir(x))
print(x.__add__)

# The __dict__ attribute -->  The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary=3456367
        
p = Person("John", 30)
print(p.__dict__)

# The help() mehthod --> The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(str))
print(help(Person))


#72. super keyword --> The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

#When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.
#e.g 1
class ParentClass:
    def parent_method(self):
        print("This is the parent method 1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("aman")
        super().parent_method()
        
    def child_method(self):
        print("This is the child method 2.")

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

#e.g 2
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        
a= employee('aman kumar',2345)
b= programmer('akash',456, 'python')
print(a.name,a.id)
print(b.name,b.id,b.lang)


#73.Magic/Dunder Methods (These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.)

#Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

# __init__ method --> The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already

# __str__ and __repr__ methods --> The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

# __len__ method --> The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

# __call__ method --> The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

from magic_method import magicmethod

e=magicmethod('aman')
print(str(e))     # calling str
print(repr(e))  # callling repr
print(e.name)
print(len(e))   #calling len
e()     # calling call

#74. Method Overriding --> Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.
#e.g- 1
class shape:                # BASE CLASS
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x*self.y
    
class circle(shape):        # DERIVED CLASS
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    
    def area(self):               # override area method
        return 3.14*super().area()
a=shape(3,4)
print(a.area())
b=circle(5)
print(b.area())

#e.g- 2
class Shape:
    def area(self):
        print("Calculating area...")
        
class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # method ovverride
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius
    
b=circle(5)
print(b.area())
        


#76. PYpdf
#77. operator overloading --> Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

# You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:
+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__

#e.g- 1

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):       # METHOD OVERLOADING
        return f"{self.i + x.i} + {self.j + x.j}j + {self.k + x.k}k"
    
a=vector(3,4,5)
print(a)        #print(str(a))
b=vector(3,6,2)
print(b)
print(a+b)

#e.g- 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.x}, {self.y}"

    def __mul__(self, other):        # METHOD OVERLOADING
        return (self.x * other.x, self.y * other.y)
    
a=Point(3,5)
print(a)
b=Point(3,7)
print(b)
print(a*b)


#78. single inheritance(Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.)
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


#79. multiple inheritence(Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.)
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

#80. multilevel inheritence(Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.)
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

#82.(pip install pypdf)
# from pypdf import PdfWriter
from pypdf import PdfWriter
merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

#83.win32com.client(text to speech)
#84. time module --> The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

#time.time() --> The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time

import time
# print(time.time())

def usingwhile():
    i=0
    while i<1001:
        print(i)
        i+=1
        
def usingfor():
    for i in range(1001):
        print(i)
        
a=time.time()
usingfor()
t1=time.time()-a

b=time.time()
usingwhile()
t2=time.time()-b

print(t1)
print(t2)

#time.sleep() --> The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads
import time

print("print now:", time.time())
time.sleep(3)
print("print after 3s:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376

# time.strftime() --> The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file,

import time
tm=time.strftime('%Y-%m-%d %H:%M:%S')
print(tm)

#85.  command line utilities
#86. walrus  --> The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
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
"""

"""
87. SHUTIL module --> Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.

Functions:-
The following are some of the most commonly used functions in the shutil module:

shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell
import shutil

# Copying a file
# shutil.copy("kbc.py", "kbcshutil.txt")

# Copying a directory
# shutil.copyfile("kbc.py", "..name.py")

# Moving a file
# shutil.move("tkinter/kbc1.py", "pdf")

# Deleting a directory
# shutil.rmtree("kbcshutil.txt")


#88. shoutout to every (pip install pypiwin32)

import win32com.client
# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Speak the desired text
speaker.Speak("Hello, this is a text-to-speech example.")


#89. request module --> The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.

#pip install request
import requests
from bs4 import BeautifulSoup

#get request
r=requests.get('https://www.google.com/')
print(r.text)

#Post Request
import requests
url = "https://api.example.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}
response = requests.post(url, headers=headers, json=data)
print(response.text)

#bs4 Module- There is another module called BeautifulSoup which is used for web scraping in Python.
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all('a'):
    print(heading.text)

#90. news api

#91. Generators--> Generator are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

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

#92. function caching --> Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.
#  function caching can be achieved using the functools.lru_cache decorator
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n*5

print(fx(2))
print("print done for 2*5\n")
print(fx(5))
print("print done for 5*5\n")
print(fx(8))
print("print done for 8*5\n")

print(fx(2))
print("print done for 2*5\n")
print(fx(5))
print("print done for 5*5\n")
print(fx(8))
print("print done for 8*5\n")

# functools.lru_cache decorator is used to cache the results of the function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size

# Benefits of Function Caching--> a significant impact on the performance of a program, particularly for computationally expensive and limited functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources and storage.


#93. news api solution
import requests
import json
query=input("plz enter your intersest fields: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-03&sortBy=publishedAt&apiKey=10d29856cc9f41b8bacabcf82e277d7f"
r=requests.get(url)
#print(r.text)
news=json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------")
    
#94. drink water remainder
#95. regular expression--> Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# Metacharacters in regular expressions:-
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs

import re
pattern= r"[a-z]+ing"
text="Regular expressions are a powerful tool for working with strings and text data in Python. Whether you're matching patterns, replacing text, or extracting, information, regular expressions make it easy to perform complex string operations with just a few lines of code. With a little bit of practice, you'll be able to use regular expressions to solve all sorts of string-related problems in Python."

#Searching for a pattern in re using re.search() Method
# match=re.search(pattern, text)
#Searching for a pattern in re using re.findall() Method
# match=re.findall(pattern,text) #Returns a list of strings
#Replacing a pattern
match=re.sub(pattern,'dog (glti se bola)', text)
print(match)

pattern= r"[a-z]+ing"
matches=re.finditer(pattern,text)  #Returns iterator of match objects
for i in matches:
    print(i)
    
    #imporatnt link-https://docs.python.org/3/library/re.html


#96. AsyncIO--> Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

import asyncio

async def function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

# async def main():
#     print(await function())
    
async def main():
    L = await asyncio.gather(
            function(),
        )
    print(L)
    
asyncio.run(main())


#97. multithreading (use to download resources paralley)--> Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds      # this is for ThreadPoolExecutor codes
t0=time.time()          #time.perf_counter()
print("time takeen to execute codes",t0)

#1st method
def main():
    # #noraml
    func(2)
    func(3)
    func(4)
    t2=time.time()
    print("time take to execute function",t2)

    print("total time take to execute",t2-t0)
    
    #Functions---The following are some of the most commonly used functions in the threading module:threading.
    # 1. threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.# 2. threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.
    # using threadiing , 2nd method
    t1=threading.Thread(target=func, args=[2])
    t2=threading.Thread(target=func, args=[3])
    t3=threading.Thread(target=func, args=[4])

    t1.start()
    t2.start()
    t3.start()
    t4=time.time()
    print("time take to threading",t4)
    print("total time take to execute",t4-t0)
# main()
    
#3rd method
# advace concept
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
    #another method to use threadpoolexecutor
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()


# Multiprocessing involves using multiple CPUs to run many processes at a time, while multithreading creates multiple threads within a single process to achieve faster and more efficient task execution.

#98. multiprocessing
import requests
import multiprocessing
import concurrent.futures

url= "https://picsum.photos/2000/3000"
def downloadfile(url,name):
    print(f"started downloading file {name}")
    response=requests.get(url)
    open(f"multiprocessing/file{name}.jpg", "wb").write(response.content)
    print(f"finished downloading {name}")
#1st method
for i in range(5):
    downloadfile(url,i)

#2nd method
pros = []
for i in range(5):
# downloadFile(url, i)
    p = multiprocessing.Process(target=downloadfile, args=[url, i])
    p.start()
    pros.append(p)
    
for p in pros:
    p.join()
    
#3rd method
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadfile, l1, l2)
    for r in results:
        print(r)
        


#99. import
from win10toast import ToastNotifier

# Create notifier object
toast = ToastNotifier()

# Show toast notification
toast.show_toast("💧 Drink Water", "Have you had water recently?", duration=6, threaded=True)

"""

#100. vote of thanks -->


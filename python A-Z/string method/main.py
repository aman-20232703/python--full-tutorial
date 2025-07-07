# main.py created inside day 13
# string method(strings are immutable , when we perform operations it can't change string, it only make copy of last strings)
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
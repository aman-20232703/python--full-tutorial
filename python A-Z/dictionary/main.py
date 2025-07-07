# main.py created inside day 33
# dictionaries(store key value items in key : value pairs tha are seperated by , and denoted {}, unordered but according to python 3.7 dict is ordered)
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
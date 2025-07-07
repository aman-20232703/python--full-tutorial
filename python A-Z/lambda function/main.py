# main.py created inside day 52
# lambda function (use in a situation where a small function is required for a short period of time, they are commanly used as argument functions such as map, filter and reduce)
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
# main.py created inside day 44
# import in python(process of loading code from python module into current script)
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

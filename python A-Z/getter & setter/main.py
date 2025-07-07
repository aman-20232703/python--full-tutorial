
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

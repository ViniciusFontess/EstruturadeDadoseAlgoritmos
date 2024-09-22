class MyClass:
    def __init__ (self,value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value})"  

    def __len__(self):
        return 355 
    
    def __eq__(self,other):
        return self.value - other.value < 5

obj = MyClass(10)
obj2 = MyClass(8)
print(repr(obj)) 
print(len(obj))    
print(obj == obj2)

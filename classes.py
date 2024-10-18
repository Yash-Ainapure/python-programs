class demo:
    def __init__(self,name):
        if name is None:
            print("constructor called without parameters")
        else:
            self.name=name
    def __str__(self):
        return "Hello "+self.name
    def __del__(self):
        print("destructor called")
    def getName(self):
         return self.name
obj=demo("yash")
print(obj)
print(obj.getName())
del obj

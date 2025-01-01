#Solution 1 ___Class___,____Name__

class SmartPhone:
    def name(self,name):
        return name

s1 = SmartPhone()
print(s1.__class__.__name__)

#Solution 2 Using type() and __name__attributes

class Smart:
    def name(self,name):
        return name
s2 = Smart()
print (type(s2).__name__)        


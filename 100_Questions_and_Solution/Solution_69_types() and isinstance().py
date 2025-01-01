#Solution 

l = [2,3,4,5,6,7]
class Smart:
    def name(self):
        pass
class Ness(Smart):
    def child(self):
        pass
obj_S =Smart()
obj_N =Ness()

print(type(obj_S)==Smart)
print(type(obj_N)==Smart)

print(isinstance(obj_S,Smart))
print(isinstance(obj_N,Smart))
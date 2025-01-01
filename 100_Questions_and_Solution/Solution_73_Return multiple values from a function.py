#Solution 1 Using Tuples

def friends():
    return "joe","Pheobe","Monica"


print(friends())
n1 , n2, n3 = friends()
print (n1,",",n2,"and",n3)

#Solution 2 Using a Dictionary
def friends():
    n1 = "joe"
    n2 = "Phoebe"

    return {1:n1,2:n2}
names = friends()    
print(names)
print(names[1],",",names[2])

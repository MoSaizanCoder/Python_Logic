#Solution 1 Using + operator

L1 = [3,6,8,2,"a","b"]
L2 = [3,6,"k","j","b"]

L12 = L1 + L2
print(L12)

#Solution 2 Using Unique Values

l12 = list(set(L1+L2))
print(l12)

#Solution 3 Using Extend() function

L1.extend(L2)
print(L1)
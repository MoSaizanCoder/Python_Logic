#Solution 
#Short a Dictionary value

marks = {"john": 23, "lisa":56, "sid": 48}

#Solution1 (Sort the dictionary based on values)

sv = sorted(marks.items(), key = lambda x : x[1])

print(sv)

#Solution 2 (sort only the values)

v= sorted(marks.values())
print(v)
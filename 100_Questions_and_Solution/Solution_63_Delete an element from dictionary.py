#Solution 1 using Delete function

marks = {"John":89,"Lisa":96,"David":65,"Peter":88}
#print(marks)
del marks["John"]
print(marks)

#Solutin 2 using pop() function
marks = {"John":89,"Lisa":96,"David":65,"Peter":88}
pop_item = marks.pop("John")
print(marks)
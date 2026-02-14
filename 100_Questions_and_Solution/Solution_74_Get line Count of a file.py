#Solution 1 Using len() function

f = open("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/file.txt")
print(len(f.readlines()))
f.close()

#Solution 2 Using list Comprehension
lines = sum(1 for i in open("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/file.txt"))
print(lines)
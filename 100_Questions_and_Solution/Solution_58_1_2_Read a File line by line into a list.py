#Solution 1 Using readlines()
f = open("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/file.txt", "r")

Lines = f.readlines()

print(Lines)

new_lines = [x.strip() for x in Lines]
print (new_lines)

#Solution 2 using for loop and list comprehension

f = open("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/file.txt", "r")

line = [line for line in f]

print(line)

new_Lines = [x.strip() for x in line]
print(new_Lines)
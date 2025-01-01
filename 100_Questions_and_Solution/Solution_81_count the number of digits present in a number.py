#Solution 1 Using while loop

num = 12345
num = int(input("Enter a Number here: "))
count = 0
while num != 0:
    num = num // 10
    count = count + 1

print(count)

#Solution 2 Using len() function

num = 12345
x = len(str(num))
print(x)
#Solution
#Sort Alphabetic Order

string = input("enter a string here: ")

split_str = string.split()
for i in range (len(split_str)):
    split_str[i] = split_str[i].lower()
split_str.sort()
#print(split_str)

for i in split_str:
    print(i)
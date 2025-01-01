#Solution Error handelling

String = input("enter string here: ")

num = int(input("enter integer here: "))

try:
    print(String + num)
except (ValueError,TypeError) as a:
    print (a) 
print ("Thank You")       
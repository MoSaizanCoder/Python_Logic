#qs 3
#count = 1
#while count <= 10:
#   print(17*count)
#  count += 1
#qs 4
#num = [1,4,9,16,25,36,49,64,81,100]
#idx = 0
#while idx < len(num):
#    print(num[idx])
#    idx += 1
#qs 5
"""
num = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0 
while i < len(num):
    if (num[i] == x):
        print("Found at idx",i)
        break
    else:
        print("finding..")
    i += 1
print("end of loop")
"""
#qs 6
"""
i = 0
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i+=1
"""
#for loop


#qs 1
#num = [1,4,9,16,25,36,49,64,81,100]
#for i in num:
#    print(i)

#qs2
#str = "apnacollege"
#
#for i in str:
#    print(i)

#qs 3
#num = [1,4,9,16,25,36,49,64,81,100]
#for i in num:
#    print(i)

#qs 4
#num = (1,4,9,16,25,36,49,64,81,100)
#
#x = 49
#
#idx = 0
#
#for el in num:
#    if (el == x):
#        print("number found at idx", idx)
#        break
#    idx += 1

#range in for loop

#qs 5

#for i in range(5):
#    print(i)
#
#for i in range(2,10):
#    print(i)
#
#for i in range(3,31,3):
#    print(i)    

#for i in range(100,0,-1):
#    print(i)
#n = int(input())
#for i in range(1,11):
#    print(n*i)
#list = [1,4,9,16,25,36,49,64,81,100,36]
#x = 36
#idx =0
#for i in list:
#    if(i == x):
#        print(x,"Found", idx)
#    idx += 1
#n = 10
#sum = 0
#i = 1
#while i <= 10:
#    sum += i
#    i += 1
#
#print(sum)
n = 5

fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)


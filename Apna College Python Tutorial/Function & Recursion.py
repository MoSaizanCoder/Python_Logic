#def avg_val(a,b,c):
#    sum = a+b+c
#    avg = sum/3
#    print(avg)
#    return avg
#
#avg_val(1,2,3)    

#cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
#heroes = ["thor", "ironman", "captain america", "shaktiman"]
#def p_list(list):
#    print(len(list))
#    return list
#p_list(cities)
#p_list(heroes)
#def print_list(list):
#    for item in list:
#        print(item, end=" ")
#
#print_list(heroes)
#print_list(cities)

#n = 5
#s = 1 
#for i in range(1,n+1):
#    s*=i
#print(s)

#def cal_fact(n):
#    fact = 1
#    for i in range(1,n+1):
#        fact*=i
#        print(fact)
#
#cal_fact(6)        
#
#def conv_currency(usd_val):
#    inr_val = usd_val*83
#    print(usd_val, "USD =", inr_val, "INR")
#    return(inr_val)
#
#conv_currency(10)    
#
#def odd_even(n):
#    if n % 2 == 0:
#        print(n, "Even")
#    else:
#        print(n, "Odd")
#
#odd_even(10)
# 
#             
#Recursion


#def sum_num(n):
#    if(n == 0):
#        return 0
#    return sum_num(n-1) + n
#sum = sum_num(5)
#print(sum)

heroes = ["thor", "ironman", "captain america", "shaktiman"]
def print_list(list,idx):
    if (idx == len(list)):
        return 0
    print(list[idx])
    print_list(list,idx+1)
print_list(heroes,0)

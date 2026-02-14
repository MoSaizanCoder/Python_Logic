#Solution
#Using Lambda Function and Filter()

l = [39,48,26,98,33,67,87]

result = (list(filter(lambda x : x % 13 == 0,l)))

print("the number is divisible by 13 are", result)
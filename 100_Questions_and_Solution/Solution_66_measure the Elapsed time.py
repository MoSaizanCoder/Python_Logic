#Solution 1 Using time Module
import time

starting_time = time.time()
num1 = int(input("Enter a number here: "))
num2 = int(input("Enter a number here: "))

print(num1 + num2)

ending_time = time.time()

print(ending_time - starting_time)

#Solution 2 Timeit module

from timeit import default_timer as timer

starting_value = timer()
num3 = int(input("Enter a number here: "))
num4 = int(input("Enter a number here: "))

print(num3 + num4)

ending_value = timer()
print(ending_value-starting_value)
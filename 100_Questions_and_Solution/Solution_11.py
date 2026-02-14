#Solution
#Program to check leap year:

year =  int(input("enter a year to check year is leap year or not: "))
if year % 4 == 0:
    print(year,"year is leap year")
else:
    print(year,"year is not leap year")
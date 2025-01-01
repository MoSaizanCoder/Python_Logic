#Solution 1Using zip() and Dictionary method:

name = ["John","Peter","Lisa","David"]
marks = [98,78,88,72]

dictionary = zip(name,marks)
print(dict(dictionary))

#Solution 2 using zip() and list comprehension

dictionaries = {key:value for key, value in zip(name,marks)}
print(dictionaries)
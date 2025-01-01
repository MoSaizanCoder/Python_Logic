#Solution
#Using List And Dictionary Comprehension

a = input("Enter a Sentence here: ")
a = a.casefold()

vowel = "aeiou"

count = {key:sum([1 for char in a if char == key])for key in vowel}

print(count)
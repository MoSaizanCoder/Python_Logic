#Solution
#Using Vowel

a = input("Enter a Sentence here: ")
a = a.casefold()

vowels = "aeiou"

count = {}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char] += 1

print(count)
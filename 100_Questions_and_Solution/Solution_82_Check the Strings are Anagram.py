#Solution
a1 = input("Enter a string here: ")
a2 = input("Enter a string here: ")
if len(a1) == len(a2):
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)


    if a1_sorted == a2_sorted:
        print("Anagrams")
    else:
        print("Not Anagrams")

else:
    print("Not Anagrams")
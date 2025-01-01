#Solution
#Iterate Over Dictionaries For Using For loop
#using.items

Friends = {"Rachel":"Ross","Monica":"Chandler","Phoebe":"Joe"}

for key, value in Friends.items():
    print(key,"-",value)

#Solution2 with keys

for key in Friends:
    print(key,":", Friends[key])

#Solution3 with keys and values

for key in Friends.keys():
    print (key)

for i in Friends.values():
    print(i)
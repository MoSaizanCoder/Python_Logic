#Solution 1 strip() function

string = " \nI Love Python"
print(string.strip(" "))

#Solution 2 Using regular expression(RegEx)

import re
string = "  I Love Python "

x = re.sub(r'^\s+|\s+$','',string)
print(x)

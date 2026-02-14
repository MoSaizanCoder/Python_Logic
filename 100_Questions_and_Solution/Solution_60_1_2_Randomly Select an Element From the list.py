#Solution Using Random Module

import random

l = [2,3,4,"a","y","p"]
random_value = random.choice(l)

print(random_value)

#SOlution 2 Using Secrets Module

import secrets
random_v = secrets.choice(l)
print(random_v)
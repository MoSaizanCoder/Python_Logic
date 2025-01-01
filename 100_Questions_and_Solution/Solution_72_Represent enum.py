#Solution

from enum import Enum

class SmartPhones(Enum):
    samsung = 1
    Nokia = 2
    Apple = 3

print(SmartPhones.samsung)    
print(SmartPhones.samsung.name)    
print(SmartPhones.samsung.value)    
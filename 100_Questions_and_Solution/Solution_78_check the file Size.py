#Solution 1 Using OS Module

import os
file_size = os.stat("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/Solution_1_1.py")

print(file_size.st_size)

#Solution 2 Using Pathlib Module

from pathlib import Path

file_size = Path("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/Solution_1_1.py")
print(file_size.stat().st_size)
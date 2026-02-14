#Solution 1 Using OS Module

import os

print(os.path.abspath(os.getcwd()))
print(os.path.dirname(os.path.abspath("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/Solution_1_1.py")))

#SOlution 2 pathlib Module

import pathlib
print(pathlib.Path().absolute())
print(pathlib.Path("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/Solution_1_1.py").parent.absolute())


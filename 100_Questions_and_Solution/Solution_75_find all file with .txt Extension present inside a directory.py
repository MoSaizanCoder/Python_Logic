#Solution 1 Uing  glob Module and os Module

import glob, os

os.chdir("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution")

for files in glob.glob("*.txt"):
    print (files)

#Solution 2 Using OS Module

import os
for files in os.listdir("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution"):
    if files.endswith(".txt"):
        print(files)

#Solution 3 Using os,Walk()
import os

for rot,dir,files in os.walk("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
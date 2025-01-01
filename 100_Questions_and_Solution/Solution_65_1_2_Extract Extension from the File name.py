#Solution 1 Using OS Module

import os
file_ext = os.path.splitext("C:/Users/91626/Desktop/Form6_S12080O6N3007241200007.pdf.pdf")
print (file_ext)
print(file_ext[1])

#Solution 2 Using pathlib Module

from pathlib import Path
file_ext = Path("C:/Users/91626/Desktop/Form6_S12080O6N")
print(file_ext.suffix)
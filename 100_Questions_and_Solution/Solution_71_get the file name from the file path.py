#Solution 1 Using OS Module

import os

file_name = os.path.basename("C:/Users/91626/Desktop/Form6_S12080O6N3007241200007.pdf.pdf")

print(os.path.splitext(file_name)[0])

#Solution 2 Using path Module

from pathlib import Path

print (Path('"C:/Users/91626/Desktop/Form6_S12080O6N3007241200007.pdf.pdf"').stem)

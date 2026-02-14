#Solution
#Resolution Of a Image
import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/91626/Desktop/FullSizeRender1.jpg")

width, height = img.size

print(width, "X", height)
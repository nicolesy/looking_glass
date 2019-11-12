
from PIL import Image
import pillow_lut

img = Image.open("ashlyn.jpg")
lut = pillow_lut.load_cube_file("Teal Orange 01 - Classic.cube")
img.filter(lut).save("temp.jpg")


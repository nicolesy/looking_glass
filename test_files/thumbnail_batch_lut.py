
from PIL import Image
import pillow_lut
import pathlib


img = Image.open("smoothie-4671.jpg")


path = pathlib.Path("./test_luts")
for cube in path.iterdir():
    if ".cube" in str(cube):
        lut = pillow_lut.load_cube_file(str(cube))
        cube = str(cube)
        cube_name = cube.replace(".cube", "")
        cube_name = cube_name.replace("test_luts/", "")
        img.filter(lut).save(cube_name + ".jpg")


    
# lut = pillow_lut.load_cube_file("Teal Orange 01 - Classic.cube")
# img.filter(lut).save("temp.jpg")


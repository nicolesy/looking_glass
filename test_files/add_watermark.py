
from PIL import Image, ImageDraw, ImageFont

 
def watermark(input_image_path, text, pos):
    photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    white = (255, 255, 255)
    font = ImageFont.truetype("HelveticaNeue.ttc", 40)
    drawing.text(pos, text, fill=white, font=font)
    photo.show()

img = "ashlyn.jpg"
watermark(img, text='nicolesy.com', pos=(20, 20))
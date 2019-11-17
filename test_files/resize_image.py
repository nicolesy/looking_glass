
from PIL import Image


basewidth = 800
img = Image.open("ashlyn.jpg")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('sompic2.jpg') 
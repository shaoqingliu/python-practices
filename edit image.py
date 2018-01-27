__author__ = 'mao'

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# msgNum = str(random.randint(1,99))    # generate a random number between 1-99
msg = "XiaoTangTang"

# Read image
im = Image.open('mao.JPG')
w,h = im.size
wDraw = 0.1 * w
hDraw = 0.4 * w

# Draw image
font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF",40)     # choose type and size
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), msg, font=font, fill=(255,87,18))

# Save image

im.save('mao.png', 'png')
im2 = im.filter(ImageFilter.SHARPEN)
im2.save('mao2.png', 'png')
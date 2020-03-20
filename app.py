from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap


def center_text(img, font, text, strip_height, strip_width, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width - text_width) / 2, strip_height)
    print(position)
    draw.text(position, text, color, font=font)
    return img


img = Image.open("res/image.jpg")
background = Image.new('RGB', (img.size[0], img.size[1] + 300), (0, 0, 0))
img_w, img_h = img.size
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save('out.png')
msg = input("enter msg")
lines = textwrap.wrap(msg, 40)
print (lines)
font = ImageFont.truetype("res/Arial.ttf", 30)
y_h = 10
c = None
for line in lines:
    width, height = font.getsize(line)
    c = center_text(background, font, line, y_h, background.size[0])
    y_h += height
c.save('sample-out.jpg')

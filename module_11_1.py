from PIL import Image, ImageDraw, ImageFont

im = Image.open('photo.jpg')

print(im.format, im.size, im.mode)
w, h = im.size
resized_im = im.resize((w, h + 100))
draw = ImageDraw.Draw(resized_im)
my_font = ImageFont.truetype('arial.ttf',40)
draw.text((100, 700), 'гора Стрельная\nСамарская область', font=my_font)
resized_im.save('new_photo.png')
resized_im.show()

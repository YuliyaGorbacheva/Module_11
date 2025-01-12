from PIL import Image, ImageDraw, ImageFont  # импорт необходимых модулей из библиотеки Pillow

im = Image.open('photo.jpg')

print(im.format, im.size, im.mode)  # вывод начальных размеров изображения
w, h = im.size
resized_im = im.resize((w, h + 100))  # изменение размера изображения, сохранение в переменную
draw = ImageDraw.Draw(resized_im)
my_font = ImageFont.truetype('arial.ttf', 40)  # определение шрифта и его размера, сохранение в переменную
draw.text((100, 700), 'гора Стрельная\nСамарская область', font=my_font)  # вставка текста в изображение
resized_im.save('new_photo.png')  # сохранение изображения в файл с новым наименованием
resized_im.show()



from PIL import Image
import pytesseract


img_path = r'Чертежи\Эталон\А4\взят из каких-то.jpg'
# img_path = r'Чертежи\Эталон\А4\ЗНГ 05 - 27 - A _ Труба А4.jpg'
img = Image.open(img_path)
img_W, img_H = img.size
# ---| get name |---
# A4_name_crop: x1 ~ 41%; x2 ~ 73.5%
#               y1 ~ 85%; y2 ~ 92.5%
x1, x2 = img_W*41/100, img_W*73.5/100
y1, y2 = img_H*85/100, img_H*92.5/100
name = img.crop((x1, y1, x2, y2))

# ---| get dec number |---
# A4_number_crop: x1 ~ 41%; x2 ~ 97%
#                 y1 ~ 80%; y2 ~ 84%
x1, x2 = img_W*41/100, img_W*97/100
y1, y2 = img_H*80/100, img_H*84/100
number = img.crop((x1, y1, x2, y2))

# ---| get entry number (входимость) |---
x1, x2 = 0, 0.308 * img_W
y1, y2 = 0, 0.218 * img_H
entry_number = img.crop((x1, y1, x2, y2))
entry_number = entry_number.rotate(-90)
img_W, img_H = x2, y2
x1, x2 = 0, img_W*0.914
y1, y2 = img_H*0.21, img_H*0.31
entry_number = entry_number.crop((x1, y1, x2, y2))

# Путь до ядра тесcеракта
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Доступные языки
# print(pytesseract.get_languages(config=''))



# Имя
text_name = pytesseract.image_to_string(name, lang='rus')
print(text_name)
name.show()


'''
# Децимальный номер
text_number = pytesseract.image_to_string(number, lang='rus')
print(text_number)
number.show()
'''

'''
# Первичная входимость
text_entry_number = pytesseract.image_to_string(entry_number, lang='rus')
print(text_entry_number)
entry_number.show()
'''




'''
# Временные файлы
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(img_path, output_folder=path)
    # img = images_from_path[0]
    # name_crop = x1 ~ 37%; y1 ~ 79%; x2 ~ 92%, y2 ~  85%
    # img_size = img.size
    # print(img.size())
    # x1 =
    # croped = images_from_path[0].crop((0, 80, 200, 400))
'''


'''
# Convert from pdf to jpg
img_path = r'Чертежи\А4\M09_069_21_002.pdf'
images = convert_from_path(img_path, dpi=200)
img = images[0]
# img.save('Чертежи\А4\M09_069_21_002.jpg')
'''

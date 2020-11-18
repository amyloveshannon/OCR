import pytesseract
from PIL import Image
from matplotlib import pyplot as plt #繪圖

image = Image.open(r'C:\Users\Egg\Desktop\RecogDigit\DigitImg\15.png')#lang='chi_tra'
code = pytesseract.image_to_string(image, lang='chi_tra', \
        config='--psm 9 --oem 3' ) ##有問題#lang='chi_tra'#config='digits'##OK: config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789

print(code)

plt.imshow(image)#有吃到照片
plt.show() 

#chi_tra: 中文繁體


#NO: 2, 4, 5
#OK: 9
#1, 3, 6, 7,->50, 
#8->9595
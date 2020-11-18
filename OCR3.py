import cv2
import pytesseract
import numpy as np 
from PIL import Image
from matplotlib import pyplot as plot #繪圖

img = Image.open(r'C:\Users\Egg\Desktop\RecogDigit\DigitImg\T5N.jpg')

plot.imshow(img)
plot.show()

#調整對比/亮度
alpha = 1.7
beta = 0
adjusted = cv2.convertScaleAbs(np.array(img), alpha=alpha, beta=beta)

plot.imshow(adjusted)
plot.show()

#轉成灰階
#轉為黑、白(0、255)
img2 = cv2.cvtColor(adjusted, cv2.COLOR_RGB2GRAY)
plot.imshow(img2, cmap="gray")
plot.show()


#侵蝕與膨脹
#膨脹與腐蝕 去除黑白點
kernel = np.ones((5, 5), np.uint8)
binary = cv2.dilate(img2, kernel, iterations=2)
binary = cv2.erode(img2, kernel, iterations=1)
plot.imshow(binary, cmap="gray")
plot.show()


code = pytesseract.image_to_string(binary, lang='eng')##有問題#config='digits'##OK: config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789

print(code)
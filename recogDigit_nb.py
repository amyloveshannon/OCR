import cv2
import pytesseract
import numpy as np 
from PIL import Image
from matplotlib import pyplot as plot #繪圖

img = Image.open(r'C:\Users\Egg\Desktop\RecogDigit\DigitImg\1112-2.jpg')
img = img.transpose(Image.ROTATE_180)#照片旋轉180度

plot.imshow(img)
plot.show()

#調整對比/亮度
alpha = 1.3  #15->1.3
beta = 0
adjusted = cv2.convertScaleAbs(np.array(img), alpha=alpha, beta=beta)

plot.imshow(adjusted)
plot.show()

//

#轉成灰階
#轉為黑、白(0、255)
img2 = cv2.cvtColor(adjusted, cv2.COLOR_RGB2GRAY)
plot.imshow(img2, cmap="gray")
plot.show()

//

#侵蝕與膨脹
#膨脹與腐蝕 去除黑白點
kernel = np.ones((5, 5), np.uint8)
binary = cv2.dilate(img2, kernel, iterations=2)#膨脹
binary = cv2.erode(img2, kernel, iterations=1)#侵蝕
plot.imshow(binary, cmap="gray")
plot.show()

//

"""
#黑白顏色轉換
from PIL import Image

img = Image.open(r'C:\Users\Egg\Desktop\RecogDigit\DigitImg\1108-27.jpg')

# 模式L”為灰色影象，它的每個畫素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
Img = img.convert('L')

plot.imshow(Img, cmap="gray")
plot.show()


# 自定義灰度界限，大於這個值為黑色，小於這個值為白色
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(1)#轉成白色
    else:
        table.append(0)#轉成黑色

# 圖片二值化
photo = Img.point(table, '1')

print(table)
plot.imshow(photo)
plot.show()

"""

//


#圖片二值化

#ret, binary = cv2.threshold(binary, 255, 0, cv2.THRESH_BINARY)
ret,binary = cv2.threshold(binary,100,110,cv2.THRESH_BINARY)
plot.imshow(binary, cmap="gray")
plot.show()


//

'''contour, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

copy_img = binary.copy()

for cnt in contour:
    x, y, w, h = cv2.boundingRect(cnt)
    print(x)
    print(y)
    print(w)
    print(h)
    plot.imshow(copy_img)
    plot.show()
    
    #cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.rectangle(copy_img, (500,1000), (1800,2000), (0,255,0), 40)#手動擷取切出興趣範圍
    
    x=500
    y=1000
    w=1800
    h=2000
    #print(x)
    #print(y)
    #print(w)
    #print(h)
   
cv2.rectangle(binary, (500,1000), (1800,2000), (0,255,0), 40)#手動擷取切出興趣範圍
plot.imshow(binary)
plot.show()''' 

//

#改變圖片大小
#cnt = max(contour, key=len)

# 裁切區域的 x 與 y 座標（左上角）
x=200
y=200
# 裁切區域的長度與寬度
w=100
h=100

print(x)
print(y)
print(w)
print(h)
#crop_img = img[y:y+h, x:x+w]  #crop_img = binary[y+100:y+h-100, x+100:x+w-100]
#crop_img = binary[250:750, 250:750]
crop_img = binary[y:y+h, x:x+w]

plot.imshow(crop_img, cmap="gray")
plot.show()

//

#模糊化
blur = cv2.medianBlur(crop_img, 5)
plot.imshow(blur, cmap="gray")
plot.show()

//

code = pytesseract.image_to_string(blur, lang='eng', \
        config='--psm 10 --oem 3')

print(code)

//

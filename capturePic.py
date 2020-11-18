import cv2
import time
import datetime
 
cap=cv2.VideoCapture(0)#選擇第1隻攝影機
today = datetime.datetime.now()
i=0
while(1):
    
    ret ,frame = cap.read()#從攝影機擷取一張影像
    k=cv2.waitKey(1)
    print(k)
    
    if k==81:
        break
    elif k==83:
        if today.month<10:#處理照片檔名
            imgMonth = "0" + str(today.month)
            imgDay = str(today.day)
        if today.day<10:
            imgMonth = str(today.month)
            imgDay = "0" + str(today.day)
        else:
            imgMonth = str(today.month)
            imgDay = str(today.day)
            
        cv2.imwrite('C:/Users/Egg/Desktop/RecogDigit/DigitImg/' + imgMonth + imgDay + "-" + str(i) + '.jpg',frame)#將擷取的影像存入
        i+=1

    cv2.imshow("capture", frame)#顯示圖片
    #time.sleep(1)#每2(s)拍一次

cap.release()#釋放攝影機
cv2.destroyAllWindows()#關閉所有 OpenCV 視窗
import cv2
import time
import datetime
 
cap=cv2.VideoCapture(0) #0表示選擇電腦第1台攝影機
today = datetime.datetime.now()
i=0
while(1):
    time.sleep(2) #讓攝影機能調整曝光、焦距等，提高照片品質，等2秒之後再拍
    ret ,frame = cap.read() #從攝影機擷取一張影像，若成功取得影像ret得到True，否則為False。影像資料存在frame變數中。
    cv2.imshow('captured_pic', frame)
    keyIn = cv2.waitKey(1) #等待1毫秒看看這時間內使用者是否按下鍵盤，存入keyIn變數: 'q:113(關閉)'、's:115(儲存)'
    print(keyIn)#-1:沒動作


    if keyIn == 113:
        break
    elif keyIn == 115:
        if today.month < 10:#處理照片檔名
            imgMonth = "0" + str(today.month)
            imgDay = str(today.day)
        if today.day < 10:
            imgMonth = str(today.month)
            imgDay = "0" + str(today.day)
        else:
            imgMonth = str(today.month)
            imgDay = str(today.day)
            
        cv2.imwrite('D:\digitRecog\Github\OCR\DigitImg\Captured\ ' + imgMonth + imgDay + "-" + str(i) + '.jpg', frame)#將擷取的影像存入
        i+=1
        #cv2.imshow('captured_pic', frame)#顯示圖片
        #time.sleep(1)#每2(s)拍一次

cap.release()#釋放攝影機
cv2.destroyAllWindows()#關閉所有 OpenCV 視窗
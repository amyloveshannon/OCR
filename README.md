#Tesseract Optical Character Recognition

tesseract OCR數字辨識、文字辨識
一般電腦字體打出來的阿拉伯數字OK，液晶的7-segment數字辨識不出來，辨識率極低，3張只成功一張，其他都辨識成字(英文字、中文字)

結論: 7-segment數字需要特別處理，tesseract無法辨識

解決方法: 1.自己訓練7-segment數字模型  2. 換一個辨識方式，不要用tesseract




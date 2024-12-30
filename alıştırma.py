import cv2
import numpy as np

resim = cv2.imread("car.jpg")
#sınır belirleme
lower = np.array([27, 100, 50])
upper = np.array([127, 255, 255])

resim= cv2.pyrDown(resim)
hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
mask= cv2.medianBlur(mask, 5)
countours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in countours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(resim,(x,y),(x+w,y+h),(0,255,0),2)

    for i in c:
        x, y = (i[0][0], i[0][1])
        print(x, y)
        resim[y, x] = [0, 255, 0]

#ağırlıklı toplam alma
toplam = cv2.addWeighted(resim, 0.7, resim, 0.3, 0)
cv2.imshow("toplam", toplam)
cv2.imshow("mask", mask)
cv2.imshow("hsv", hsv)

#gürültü azaltma
resim = cv2.fastNlMeansDenoising(resim, None, 10, 7, 21)

#yazı yazma
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(resim, "formula", (100, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
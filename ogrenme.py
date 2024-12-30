import cv2
import numpy as np  

resim = cv2.imread("car.jpg")
 #bir bölgeyi beyaz yapma
for i in range( 100):
        for j in range(100):
            resim[i, j] = [255, 255, 255]    

#bir bölgeye efekt atma 
resim[150:200, 150:200, 1] = 150     

#resimden kesit alma ve kesiti başka bir yere yerleştirme
kesit = resim[70:100, 100:130]
resim[60:90, 50:80] = kesit

#resmin bir kısmına efekt uygulama
resim[100:200, 200:300, 0] = 255
 
#resme yazı yazma
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(resim, "formula", (100, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

#resmin bir kısmına kare çizme
cv2.rectangle(resim, (50, 50), (100, 100), (255, 0, 0), 2)

#resmin bir kısmına daire çizme
cv2.circle(resim, (200, 200), 50, (0, 255, 0), 2)

#histogram eşitleme
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
resim = cv2.equalizeHist(resim)


#gürültü ekleme
gurultu = np.random.randint(0, 255, resim.shape)

#istenmedik yerleri siyah yapma
resim[0:50, 0:50] = 0

#contrast arttırma
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
resim = clahe.apply(resim)


cv2.imshow("resim", resim)  

print("resmin özellikleri: " +str(resim.shape))
print("resmin boyutu: " +str(resim.size)) 
print("resmin veri tipi: " +str(resim.dtype)) 


cv2.waitKey(0)  
cv2.destroyAllWindows() 


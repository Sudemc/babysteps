import cv2
import numpy as np

#kameradan görüntü alma
kamera = cv2.VideoCapture(0)
while True:
    ret, görüntü = kamera.read()
    cv2.imshow("kamera", görüntü)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()

#canlı görüntüye şekiller ve çizgi ekleme
kamera = cv2.VideoCapture(0)
while True:
    ret, görüntü = kamera.read()

    cv2.rectangle(görüntü, (100, 100), (200, 200), (255, 0, 0), 2)
    cv2.line(görüntü, (100, 100), (200, 200), (0, 255, 0), 2)
    cv2.circle(görüntü, (150, 150), 50, (0, 0, 255), 2)
    cv2.putText(görüntü, "formula", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("kamera", görüntü)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
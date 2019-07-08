import numpy as np
import cv2

star_cascade = cv2.CascadeClassifier('cascadetest1.xml')

img = cv2.imread("stellarium-000.png")
cv2.imshow("cap", img)

while 1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # add this
    # image, reject levels level weights.
    stars = star_cascade.detectMultiScale(gray, 50, 50)
    
    # add this
    for (x,y,w,h) in stars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

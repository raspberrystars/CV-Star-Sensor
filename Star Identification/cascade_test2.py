#This is an updated script, removed some unnecessary code.

import numpy as np
import cv2

stars_cascade = cv2.CascadeClassifier('cascadetest57.xml')

img = cv2.imread('stellarium-001-fiducial6-blended.png')

while 1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    stars = stars_cascade.detectMultiScale(gray, 1.05, 50)
    
    for (x,y,w,h) in stars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        
    cv2.waitKey(0)

    cv2.imshow('img',img)


cap.release()
cv2.destroyAllWindows()

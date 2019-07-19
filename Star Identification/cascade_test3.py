#Updated to show only the largest detected box.

import numpy as np
import cv2

stars_cascade = cv2.CascadeClassifier('cascadetest57.xml')

img = cv2.imread('stellarium-001-fiducial6-blended.png')

big_w = 1
big_h = 1

while 1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    stars = stars_cascade.detectMultiScale(gray, 1.05, 50)
    
    for (x,y,w,h) in stars:
        if w > big_w:
            big_w = w
            correct_x = x
            correct_y = y
        
    cv2.rectangle(img,(correct_x,correct_y),(correct_x+big_w,correct_y+big_w),(255,255,0),2)
    cv2.waitKey(0)
    cv2.imshow('img',img)

cap.release()
cv2.destroyAllWindows()

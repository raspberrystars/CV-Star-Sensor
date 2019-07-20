#Improvement of cascade_test5, designed to display the box with highest levelWeight value.

import cv2
import numpy as np

stars_cascade1 = cv2.CascadeClassifier('cascadetest63.xml')

img = cv2.imread("stellarium-016-multitest.png")


stars1, rejectLevels1, levelWeights1 = stars_cascade1.detectMultiScale3(
    img,
    scaleFactor=1.02,
    minNeighbors=10,
    flags=0,
    minSize=(200, 200),
    maxSize=(400,400),
    outputRejectLevels = True
    )

##print(levelWeights)
i = 0
highweight = 0

for (x,y,w,h) in stars1:

    if levelWeights1[i] > highweight:
        highweight = levelWeights1[i]
        x1 = x
        y1 = y
        w1 = w
        h1 = h
    
    i = i+1


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,str(highweight[0]),(x1,y1+h1+22), font,0.7,(255,255,255),2,cv2.LINE_AA)
cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,255),2)

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

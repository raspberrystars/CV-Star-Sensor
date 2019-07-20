#Improvement of cascade_test7, now for two cascades simultaneously.
#Same as cascade_test7, it only displays the box with the highest levelWeight value.

import cv2
import numpy as np

stars_cascade1 = cv2.CascadeClassifier('cascadetest63.xml')
stars_cascade2 = cv2.CascadeClassifier('cascadetest64.xml')

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

stars2, rejectLevels2, levelWeights2 = stars_cascade2.detectMultiScale3(
    img,
    scaleFactor=1.02,
    minNeighbors=200,
    flags=0,
    minSize=(200, 200),
    maxSize=(500,500),
    outputRejectLevels = True
    )

##print(levelWeights)
i = 0
highweight1 = 0
highweight2 = 0

for (x,y,w,h) in stars1:

    if levelWeights1[i] > highweight1:
        highweight1 = levelWeights1[i]
        x1 = x
        y1 = y
        w1 = w
        h1 = h
    
    i = i+1

i = 0
for (x,y,w,h) in stars2:

    if levelWeights2[i] > highweight2:
        highweight2 = levelWeights2[i]
        x2 = x
        y2 = y
        w2 = w
        h2 = h
    
    i = i+1

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,'STAR PATTERN 1',(x1,y1-10), font,0.7,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,str(highweight1[0]),(x1,y1+h1+24), font,0.7,(255,255,255),2,cv2.LINE_AA)
cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)

cv2.putText(img,'STAR PATTERN 2',(x2,y2-10), font,0.7,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,str(highweight2[0]),(x2,y2+h2+24), font,0.7,(255,255,255),2,cv2.LINE_AA)
cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Modification of cascade_test5, now for two cascades simultaneously.

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
    maxSize=(500,500),
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
font = cv2.FONT_ITALIC

for (x,y,w,h) in stars1:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(levelWeights1[i][0]),(x,y+h+22), font,0.7,(255,255,255),2,cv2.LINE_AA)
    i = i+1

i = 0

for (x,y,w,h) in stars2:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(levelWeights2[i][0]),(x,y+h+22), font,0.7,(255,255,255),2,cv2.LINE_AA)
    i = i+1

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

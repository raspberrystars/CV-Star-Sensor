#Imports required libraries.
import cv2
import numpy as np
import os, os.path

#Creates variables for position and RA/Dec coordinate for two detections.
d1x, d1y, d1ra, d1dec, d2x, d2y, d2ra, d2dec = (0,)*8

#Loads an input test image (which has had fiducial markers applied).
#In practice an image would be received from the RPi camera and markers applied.
img = cv2.imread('stellarium-169-markers.png')

#Creating a detection function.
def stardetection(cascade, ra, dec, minn, sf):
    #Specifies the cascade file to be loaded.
    stars_cascade = cv2.CascadeClassifier('realcascades/weighted_purged/'+cascade+','+ra+','+dec+','+minn+','+sf+'.xml')
    
    #Applies the detectMultiScale3 function with the appropriate parameters.
    stars, rejectLevels, levelWeights = stars_cascade.detectMultiScale3(
        img,
        scaleFactor = 1.05,
        minNeighbors = int(minn),
        flags = 0,
        minSize = (300, 300),
        maxSize = (400, 400),
        outputRejectLevels = True
        )

    #Create some additional variables = 0 for use in later 'for loops'.
    i = 0
    highweight = 0
    big_w = 0
    weighted = 0

    #The purpose of this if statement is to see if any detection has been made.
    if(len(stars) > 0):
        for (x,y,w,h) in stars:

            #This if statement will find the detection with the largest bounding box.
            if w > big_w:
                highweight = levelWeights[i]
                weighted = float(highweight)*float(sf)
                x1 = x
                y1 = y
                w1 = w
                h1 = h

        #The if statement below sets the levelWeights value bounds for a 'successful' detection.
        if (weighted > 4) and (weighted < 6):
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,cascade,(x1,y1-16), font,0.9,(0,0,255),2,cv2.LINE_AA)
            cv2.putText(img,str(weighted),(x1,y1+h1+25), font,0.7,(0,0,255),2,cv2.LINE_AA)
            cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
            cenpixx = int(x1 + 0.5 * w1)
            cenpixy = int(y1 + 0.5 * h1)
            cv2.putText(img,str(cenpixx)+', '+str(cenpixy),(x1,y1-45), font,0.9,(0,0,255),2,cv2.LINE_AA)
            shrunk_img = cv2.resize(img, (1344, 756))
            cv2.imshow("Star Pattern Detections",shrunk_img)
            print('Cascade number '+cascade+' DETECTS')
            print(weighted)
            print()

            #Pulls in the global variables for the pixel and world coordinates of the detections.
            global d1x, d1y, d1ra, d1dec
            global d2x, d2y, d2ra, d2dec

            #The following statements assign the parameters of two successful detection to those variables.
            if (d1x == 0):
                d1x = cenpixx
                d1y = cenpixy
                d1ra = ra
                d1dec = dec
            else:
                d2x = cenpixx
                d2y = cenpixy
                d2ra = ra
                d2dec = dec
        else:
            print('Cascade number '+cascade+' POOR DETECTION')
            print(weighted)
            print()
    else:
        print('Cascade number '+cascade+' NO DETECTION')
        print()
    return(d1x, d1y, d1ra, d1dec, d2x, d2y, d2ra, d2dec)

#Runs the detection function for each cascade file within the specified folder.
for file in ['realcascades/weighted_purged']:
    for item in os.listdir(file):
        item = os.path.splitext(item)[0]
        items = item.split(',')
        first = int(items[0])
        second = str(items[-4])
        third = str(items[-3])
        fourth = int(items[-2])
        fifth = str(items[-1])

        stardetection(cascade = str(first), ra = second, dec = third, minn = str(fourth), sf = fifth)

#Prints the returned pixel coordinates and RA/Dec coordinates for two positive IDs from the stardetection fn.
print(d1x, d1y)
print(d1ra, d1dec)
print()
print(d2x, d2y)
print(d2ra, d2dec)
print()

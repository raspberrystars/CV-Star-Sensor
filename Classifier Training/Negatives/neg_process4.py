#Imports required libraries
import cv2
import os, os.path

#Assumes 1920x1080 pixel input Stellarium screenshot.
#The following coordinates allow a 1080x1080 square image to be cropped.
y=0
x=420
h=1080
w=1080

#A stage counter used to name files.
picno = 1

#Location of the Stellarium screenshots to be processed.
path = "E:/Documents/Strathclyde/Thesis/Stellarium Screenshots/Northern Celestial Hemisphere/"
path_list = []

#Creates full file location for each file within that specified folder.
for file in os.listdir(path):
    extension = os.path.splitext(file)[1]
    path_list.append(os.path.join(path, file))

#For each file, crops to square, greyscales, and shrinks to 100x100 pixels.
#Each image is then saved as a number .jpg
for imagePath in path_list:
    imgstart = cv2.imread(imagePath)
    crop_img = imgstart[y:y+h, x:x+w]
    grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    shrunk_img = cv2.resize(grey_img, (100, 100))
    image_name = str(picno)+'.jpg'
    cv2.imwrite(image_name, shrunk_img)
    #cv2.imshow(imagePath, shrunk_img)
    picno += 1


    
    

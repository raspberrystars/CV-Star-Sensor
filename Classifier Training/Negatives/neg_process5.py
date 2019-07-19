import cv2
import os, os.path

y=0
x=420
h=1080
w=1080

picno = 1

path = "E:/Documents/Strathclyde/Thesis/Stellarium Screenshots/Northern Celestial Hemisphere/"
path_list = []

for file in os.listdir(path):
    extension = os.path.splitext(file)[1]
    path_list.append(os.path.join(path, file))

for imagePath in path_list:
    imgstart = cv2.imread(imagePath)
    crop_img = imgstart[y:y+h, x:x+w]
    grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(grey_img, 225, 255, cv2.THRESH_BINARY)[1]
    mask = thresh.copy()
    mask = cv2.dilate(mask, None, iterations=2)
    shrunk_img = cv2.resize(mask, (100, 100))
    mask2 = shrunk_img.copy()
    mask2 = cv2.dilate(mask2, None, iterations=1)
    image_name = str(picno)+'.jpg'
    cv2.imwrite(image_name, mask2)
    picno += 1
    cv2.waitKey(0)


    
    

import cv2
import os, os.path

y=100
x=370
h=700
w=700

picno = 1

path = "E:/Documents/Strathclyde/Thesis/Python Programs/training_test3/Samples/"
path_list = []

for file in os.listdir(path):
    extension = os.path.splitext(file)[1]
    path_list.append(os.path.join(path, file))

for imagePath in path_list:
    imgstart = cv2.imread(imagePath)
    crop_img = imgstart[y:y+h, x:x+w]
    grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    shrunk_img = cv2.resize(grey_img, (100, 100))
    image_name = 'neg'+str(picno)+'.jpg'
    cv2.imwrite(image_name, shrunk_img)
    #cv2.imshow(imagePath, shrunk_img)
    picno += 1


    
    

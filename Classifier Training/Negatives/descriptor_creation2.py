#Imports required libraries.
import cv2
import os

#Specifies location of neg folder.
if not os.path.exists('neg_southern2'):
    os.makedirs('neg_southern2')

#Loops over each negative file in that folder.
#Creates .txt file with names of these files.
for file in ['neg_southern2']:
    for img in os.listdir(file):
        line = img+'\n'
        with open('bg.txt','a') as f:
            f.write('neg/' + line)

    

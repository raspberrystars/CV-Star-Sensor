import cv2
import os

if not os.path.exists('neg_southern'):
    os.makedirs('neg_southern')

for file in ['neg_southern']:
    for img in os.listdir(file):
        line = img+'\n'
        with open('bg.txt','a') as f:
            f.write('neg/' + line)

    

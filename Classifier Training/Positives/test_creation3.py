#note that this was the program used to generate the six folders of the initial
#fiducial tests. It was upgraded to test_creation5 to use with fiducial 6 blending

import imutils
import cv2

fg_img = cv2.imread("fiducial_6_80x80.png", cv2.IMREAD_UNCHANGED)
bg_img = cv2.imread("stellarium-005.png")

graybg = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(graybg, 225, 255, cv2.THRESH_BINARY)[1]
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=1)
mask2 = mask.copy()
mask2 = cv2.dilate(mask2, None, iterations = 2)
h2, w2 = mask2.shape[:2]

cnts = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

fgy, fgx = fg_img.shape[:2]

alpha_s = fg_img[:, :, 3] / 255.0
alpha_l = 1.0 - alpha_s

for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        y1 = y - 40
        y2 = y1 + fgy
        
        x1 = x - 40
        x2 = x1 + fgx


        if h2 - y1 > fgy + 1 and y1 > fgy + 1 and w2 - x1 > fgx + 1 and x1 > fgx + 1:
                for c in range(0, 3):
                        bg_img[y1:y2, x1:x2, c] = (alpha_s * fg_img[:, :, c] + alpha_l * bg_img[y1:y2, x1:x2, c])

y=390
x=810
h=300
w=300

crop_img = bg_img[y:y+h, x:x+w]
grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
shrunk_img = cv2.resize(grey_img, (50, 50))
small_image_name = 'postest59.jpg'
cv2.imwrite(small_image_name, shrunk_img)

big_image_name = 'stellarium-005-fiducial6.png'
cv2.imwrite(big_image_name, bg_img)

##cv2.imshow("Final", bg_img)
cv2.waitKey(0)

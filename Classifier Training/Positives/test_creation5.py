#This program was developed from test_creation3 in order to blend fiducials.
#Only works perfectly with fiducial 6.

import imutils
import cv2

fg_img = cv2.imread("fiducial_6_80x80.png", cv2.IMREAD_UNCHANGED)
bg_img = cv2.imread("stellarium-005.png")
rectangle = cv2.imread("rectangle_black.png")

graybg = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(graybg, 225, 255, cv2.THRESH_BINARY)[1]
mask1 = thresh.copy()
mask1 = cv2.erode(mask1, None, iterations=1)
mask2 = mask1.copy()
mask2 = cv2.dilate(mask2, None, iterations = 2)
h2, w2 = mask2.shape[:2]

cnts = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

fgy, fgx = fg_img.shape[:2]

alpha_s = fg_img[:, :, 3] / 255.0
alpha_l = 1.0 - alpha_s

rectangle_build = rectangle.copy()


for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        y1 = y - 40
        y2 = y1 + fgy
        
        x1 = x - 40
        x2 = x1 + fgx

        rectangle_temp = rectangle.copy()

        if h2 - y1 > fgy + 1 and y1 > fgy + 1 and w2 - x1 > fgx + 1 and x1 > fgx + 1:
                for c in range(0, 3):
                        rectangle_temp[y1:y2, x1:x2, c] = (alpha_s * fg_img[:, :, c] + alpha_l * rectangle[y1:y2, x1:x2, c])

                rows,cols,channels = rectangle_temp.shape
                roi = rectangle_build[0:rows, 0:cols ]
                img2gray = cv2.cvtColor(rectangle_temp,cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)        
                img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
                img2_fg = cv2.bitwise_and(rectangle_temp,rectangle_temp,mask = mask)
                dst = cv2.add(img1_bg,img2_fg)
                rectangle_build[0:rows, 0:cols ] = dst


rows,cols,channels = rectangle_build.shape
roi = bg_img[0:rows, 0:cols ]
img2gray = cv2.cvtColor(rectangle_build,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(rectangle_build,rectangle_build,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
bg_img[0:rows, 0:cols ] = dst


##cv2.imshow("first", bg_img)
##cv2.waitKey(0)

                        
y=390
x=810
h=300
w=300

crop_img = bg_img[y:y+h, x:x+w]
grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
shrunk_img = cv2.resize(grey_img, (50, 50))
small_image_name = 'postest65.jpg'
cv2.imwrite(small_image_name, shrunk_img)

big_image_name = 'stellarium-005-fiducial6-blended.png'
cv2.imwrite(big_image_name, bg_img)

##cv2.imshow("Final", bg_img)
cv2.waitKey(0)

#Imports required libraries.
import imutils
import cv2

#Loads images of the fiducial marker, the background star image, and a black rectangle.
#The black rectangle is of the same resolution as bg_img.
fg_img = cv2.imread("fiducial_6_80x80.png", cv2.IMREAD_UNCHANGED)
bg_img = cv2.imread("filename.png")
rectangle = cv2.imread("rectangle_black.png")

#Enlarges bg_img to prevent erosion stage from removing too many stars.
enlarged_big = cv2.resize(bg_img, (3840, 2160))

#Greyscales the enlarged background star image.
graybg = cv2.cvtColor(enlarged_big, cv2.COLOR_BGR2GRAY)

#Thresholds, erodes, and dilates the stars on this image.
thresh = cv2.threshold(graybg, 175, 255, cv2.THRESH_BINARY)[1]
mask1 = thresh.copy()
mask1 = cv2.erode(mask1, None, iterations=1)
mask2 = mask1.copy()
mask2 = cv2.dilate(mask2, None, iterations = 2)

#Resizes back to original resolution, and finds the dimensions.
mask2resized = cv2.resize(mask2, (1920, 1080))
h2, w2 = mask2resized.shape[:2]

#Identifies 'contours' within the processed image.
cnts = cv2.findContours(mask2resized.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#Finds the dimensions of the fiducial marker image.
#This image is a circular markers on a rectangular transparent background.
fgy, fgx = fg_img.shape[:2]

#Handles the alpha channel of the fiducial marker image, needed for the transparency.
alpha_s = fg_img[:, :, 3] / 255.0
alpha_l = 1.0 - alpha_s

rectangle_build = rectangle.copy()

#For each identified contour (bright star), applies a fiducial marker to that location.
#Adds the fiducial markers to the black rectangle. 
for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        y1 = int((y + 0.5 * h) - 0.5 * fgy)
        y2 = y1 + fgy
        
        x1 = int((x + 0.5 * w) - 0.5 * fgx)
        x2 = x1 + fgx

        rectangle_temp = rectangle.copy()

        if y1 > 0 and y2 < h2 and x1 > 0 and x2 < w2:
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

#Merges the rectangular image with fiducial markers onto the background sky image. 
rows,cols,channels = rectangle_build.shape
roi = bg_img[0:rows, 0:cols ]
img2gray = cv2.cvtColor(rectangle_build,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(rectangle_build,rectangle_build,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
bg_img[0:rows, 0:cols ] = dst

#Specifies area of main image to crop for positive image.                     
y=390
x=810
h=300
w=300

#Crops section of main image with markers, names it positive file and saves.
crop_img = bg_img[y:y+h, x:x+w]
grey_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
shrunk_img = cv2.resize(grey_img, (50, 50))
small_image_name = 'positive.jpg'
cv2.imwrite(small_image_name, shrunk_img)

#Names and creates a test file which cascades trained on this positive image can be checked against.
big_image_name = 'filename2.png'
cv2.imwrite(big_image_name, bg_img)

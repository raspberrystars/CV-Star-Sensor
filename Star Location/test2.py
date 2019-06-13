# This program locates and counts stars in a given .png image
# Also included is an optional erosion stage to isolate the brightest stars
# Also included is an optional dilation stage to magnfiy them

# import the necessary packages
import imutils
import cv2

# load and display the input image
image = cv2.imread("sample3.png")
cv2.imshow("Image", image)
#cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
#cv2.waitKey(0)

# applying edge detection 
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
#cv2.waitKey(0)

# threshold the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Thresh", thresh)
#cv2.waitKey(0)

#erosion step
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=1)
cv2.imshow("Eroded", mask)
#cv2.waitKey(0)

#dilation step
mask2 = mask.copy()
mask2 = cv2.dilate(mask2, None, iterations = 2)
cv2.imshow("Dilated", mask2)
#cv2.waitKey(0)

# find contours 
cnts = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

# find centre point of each contour (star)
for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x,y), (x + w, y + h), (0, 255, 0), 2)
        centre = (x,y)
        cv2.line(output, (0,0), (x,y), (255, 0, 0), 1, 8, 0)
        cv2.imshow("Contours", output)
        print(centre)

# loop over the contours
for c in cnts:
	cv2.drawContours(output, [c], -1, (0, 0, 255), 4)
	cv2.imshow("Contours", output)

# draw the total number of contours found 
text = "There are {} bright stars".format(len(cnts))
cv2.putText(output, text, (10, 35),  cv2.FONT_HERSHEY_COMPLEX, 1.2,
	(0, 0, 255), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

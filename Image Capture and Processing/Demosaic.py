import numpy as np
imsize = imrows*imcols
with open(infile, "rb") as rawimage:
    img = np.fromfile(rawimage, np.dtype('u1'), imsize).reshape((imrows, imcols))
    colour = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    

import matplotlib
from matplotlib import pyplot as plt
import picamraw

raw_bayer=picamraw.PiRawBayer(
filepath='home/pi/Documents/Thesis/Photography/raw.jpeg', camera_version=PiCameraVersion.V2)
plt.imshow(raw_bayer.to-rgb())

from matplotlib import pyplot as plt
import picamraw

raw_bayer=picamraw.PiRawBayer(
    filepath='/pi/home/Documents/Thesis/Photography/image.jpeg',
    camera_version=PiCameraVersion.V2,
    )

plt.imshow(raw_bayer.to_rgb())


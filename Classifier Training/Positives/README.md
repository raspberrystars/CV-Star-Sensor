## Description of the contents of this folder

The python program is used to generate the 50x50 positive image used for the cascade training process. The method by which this happens is firstly the bright stars in an input image are identified, then a marker with a transparent background is placed onto each pixel coordinate where the bright stars are located. 

**test_creation7** - the latest iteration of this program. The image files also in this folder are required for the process, as would also be an input sample star image from Stellarium. This was designed for a resolution of 1920x1080 on those images. It is a good idea to set a magnitude limit of 5.0 in Stellarium, to limit the star count visible, which is also considered representative of the level of stars visible by a typical star sensor camera.

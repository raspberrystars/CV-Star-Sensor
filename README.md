## CV-Star-Sensor

# MSc Project repo for computer vision star identification and satellite orientation project (CURRENTLY ACTIVE)

This repository shall be used to store all versions of the code generated as part of this project.

**Contents so far:**
- Stellarium scripts used to capture thousands of images from Stellarium in order to be processed into negative image datasets for machine learning training.
- Zipped folders containing negative image datasets, as well as bg.txt files, and python programs used to create these.
- Python programs used to create the positive images used for cascade training. 
- Image files of the fiducial markers applied to starfields, to identify the patterns of bright stars that the machine learning relies upon for the identification.
- Python programs used to test the trained cascades against a supplied starfield image.

**Additional contents shall be:**
- Detailed project wiki.
- Final set of trained cascade .xml files used for star identification.
- Python programs that can utilise such cascades to correctly provide the orientation of the simulated camera relative to the stars.
- Additional information about opencv setup, and test data.

## Description of the scripts in this folder

**Instructions:** To use these scripts, place them in the scripts folder of your Stellarium install folder (most likely under Program Files). They can be run either from within Stellarium by opening the scripts window, or by simply running the scripts from the scripts folder, which will open up Stellarium and run them. 

**Purpose:** These scripts are used to capture a large number (just under 2000) images of starfields from within Stellarium. Screenshots are saved, which can then be processed using python and opencv into the negative image datasets used for cascade training. The scripts configure Stellarium to display the sky as appropriate, and then pan through a large sequence of Ra/Dec coordinates, capturing screenshots (with a small delay in-between to not overload). 

**thesis_4** - captures images of the northern celestial hemisphere. Takes approx. 1/2 hour to run on moderately powerful PC.

**thesis_5** - captures images of the southern celestial hemisphere. Takes approx 1/2 hour to run on moderately powerful PC.

**thesis_setup** - this just runs the sky configuration part of the above programs but without the automatic panning and screenshot capture. Useful for setting up Stellarium to be appropriate for manually capturing test images.

# python-for-hydrology

A fork of a course!

## Python USGS NYWSC Training Agenda Spring 2023

### Tuesday
- 0800-0830: Introductions and getting started
- 0830-0900: Python overview and Quick orientation to conda environments and jupyter
- 0900-1030: 00 Python basics review: Q&A and discussion https://cscircles.cemc.uwaterloo.ca/  (A: word counting )
- 1030-1100: break
- 1100-1200: 01 Functions and Scripts  (A: build a function)
- 1200-1300: lunch
- 1300-1500: 03 Useful Standard Library modules
- 1500-1530: break
- 1530-1700: 04 Working with files, string formatting 
- 1700: Class adjourn
 
### Wednesday
- 0800-1000: 05 Numpy (where, slicing, indexing, ….)(A: Mt. St. Helens)
- 1000-1030: break
- 1030-1200: 06 Matplotlib (A: make a semi-complex plot, animation, PdfPages)
- 1200-1300: lunch
- 1300-1430: 08 Pandas (interesting data, viz, excel, apply correction to data, indexing, grouping, retrieving data from NWIS (various approaches), Raul’s https://github.com/raoulcollenteur/Python-Hydrology-Tools
- 1430-1500: break
- 1500-1700: 09 GeoPandas for open-source GIS (A: working with open-source city data)
- 1700: Class adjourn

### Thursday
- 0800-1000: 10 Rasterio 
- 1000-1030: break
- 1030-1200: 12 Cartopy and USGS-style Figures
- 1200-1300: lunch
- 1300: Class adjourn, but work/discussion time if folks want


## Installation Instructions

### Download the course repository:

You can do this in one of two ways. 
1. (easier) Download the repo as a zip file by clicking on the green "Code" button at the top of the page and selecting "Download ZIP".  Unzip the folder and work from there.
2. (requires familiarity with Git) Install Git following directions here: [Git](https://gitforwindows.org/). Sign-up for a Github account, then clone the the repo.

### Install Python and dependencies:
1. If you have already installed Python using Anaconda, you can skip this step. If not, install [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links) by following that link and selecting the correct OS installer (likely Windows 64-bit). It's best to install Miniconda for the local user, which does not require admin permissions.
2. If you are using __Windows__: go to the start menu and open "Anaconda Powershell Prompt". An Anaconda command line window will open. (On __Linux__ or __MacOS__, just use the standard terminal.) Navigate to the course repo folder on your machine. You can accomplish this by typing `cd your/folder/path` and pressing < enter >. Replace `your/folder/path` with the path to the course material folder on your computer (you can copy the path from the address bar in File Explorer). .
3. Next, type `conda env create -f environment.yml`. This will create an anaconda environment called "pyclass" and install the python dependencies required for this course. It may take a while, a good time to grab some coffee! If a Windows prompt comes up requesting admin credentials, just exit the prompt. Everything should still install correctly. You can inspect the *environment.yml* file in the repo folder to see what is being installed.

### Start jupyter notebook
You will need to do this step any time you wish to open one of the course notebooks.

To start up the jupyter notebook:
- Windows: open Anaconda Powershell prompt and type `conda activate pyclass`
- Mac/Linux: open a terminal and type `conda activate pyclass`
- Then navigate to the folder (use `cd`!) where you downloaded the course materials repo and type `jupyter lab`
A jupyter notebook instance should start within the course repo flder. Using the built-in browser, you can now navigate to the "notebooks" folder and open one.

# python-for-hydrology

A fork of a course!

## Python USGS NYWSC Training Agenda

### Tuesday
- 0800-0830: Introductions and getting started
- 0830-0900: Python overview and Quick orientation to conda environments and jupyter
- 0900-1030: 00 Python basics review: Q&A and discussion https://cscircles.cemc.uwaterloo.ca/  (A: word counting )
- 1030-1100: break
- 1100-1200: 01 Functions and Scripts  (A: build a function)
- 1200-1300: lunch
- 1300-1500: 02 Namespace, Modules, Packages, Objects (A: import and use own functions, etc) 
- 1500-1530: break
- 1530-1630: 03 Useful Standard Library modules
- 1630-1700: 04 Working with files, string formatting 
- 1700: Class Adjourn 
 
### Wednesday
- 0800-0830:  04 Working with files, string formatting (continued)
- 0830-1030: 05 Numpy (where, slicing, indexing, ….)(A: Mt. St. Helens)
- 1030-1100: break
- 1100-1200: 06 Matplotlib (A: make a semi-complex plot, animation, PdfPages)
- 1200-1300: lunch
- 1300-1400: 06 Matplotlib(A: make a semi-complex plot, animation, PdfPages)(continued)
- 1400-1430: break
- 1430-1600: 07 Theis exercise + VSCode IDE debugging, liveshare
- 1600-1700: 08 Pandas (interesting data, viz, excel, apply correction to data, indexing, grouping, retrieving data from NWIS (various approaches), Raul’s https://github.com/raoulcollenteur/Python-Hydrology-Tools 
- 1700: Class Adjourn

### Thursday
- 0800-0900: 08 Pandas (interesting data, viz, excel, apply correction to data, indexing, grouping, retrieving data from NWIS (various approaches), Raul’s https://github.com/raoulcollenteur/Python-Hydrology-Tools (continued)
- 0900-1030: 09 GeoPandas for open-source GIS
- 1030-1100: break
- 1100-1130: 09 GeoPandas for open-source GIS (A: working with open-source city data) (continued)
- 1130-1200: 10 Rasterio 
- 1200-1300: lunch
- 1300-1400: 10 Rasterio (continued)
- 1400-1430: break
- 1430-1600: 11 Xarray
- 1600-1700: Wrap-up: Pointing to some other packages
- 1700: class adjourn


## Installation Instructions

### Download the course repository:

You can do this in one of two ways. 
1. (easier) Download the repo as a zip file by clicking on the green "Code" button at the top of the page and selecting "Download ZIP".  Unzip the folder and work from there.
2. (recommended; but requires familiarity with Git). Install Git following directions here: [Git](https://gitforwindows.org/). Sign-up for a Github account, then clone the the repo.

### Install Python and dependencies:
1. If you have already installed Python using Anaconda, you can skip this step. If not, install [Anaconda](https://www.anaconda.com/products/individual) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), if you prefer)
2. If you are using __Windows__: go to the start menu and open "Anaconda prompt". An anaconda command line window will open. (On __Linux__ or __MacOS__, just use the standard terminal.) Navigate to the course repo folder on your machine. You can accomplish this by typing `cd your/folder/path` and pressing < enter >. Replace `your/folder/path` with the path to the course material folder on your computer.
3. Next, type `conda env create -f environment.yml`. This will create an anaconda environment called "pyclass" and install the python dependencies required for this course. It may take a while. Should you wish, you can inspect the *environment.yml* file in the repo folder to see what dependecies are being installed.

### Start jupyter notebook
You will need to do this step any time you wish to open one of the course notebooks.

To start up the jupyter notebook:
- Windows: open the Anaconda prompt and type `conda activate pyclass`
- Mac/Linux: open a terminal and type `conda activate pyclass`
- Then navigate to folder where you downloaded the course materials repo and type `jupyter notebook`
A jupyter notebook instance should start within the course repo flder. Using the browser, you can now navigate to the "notebooks" folder and open one.

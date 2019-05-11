# OS_Screenshot
OS_Screenshot is used as a way to create a pdf for undownloadable (read-only) pdf files.

## Setup
Two external libraries are used for these scripts - pyautogui and fpdf. <br/>
To install pyautogui, check the following link: https://pyautogui.readthedocs.io/en/latest/install.html <br/>
To install fpdf, check the following link: https://pypi.org/project/fpdf/

## Usage
These scripts are best run using the command line.

### mouse_positions.py
This script outputs the coordinates of where your cursor is on the screen until terminated. This is useful when getting the region of the screen to screenshot which is used in the script pdf_screenshot.py. 

### pdf_screenshot.py 
This script takes a screenshot of every page of the pdf. Before pressing Enter on the command line to run this script, make sure that the command line window is not fully maximized and that it is over the window with the pdf. Hover the cursor on the part of the screen that is not on the command line window, then press Enter to run the script. Doing so would let the script move to the pdf window. All screenshots are saved as .png files in a folder called images. The number of pages and region of the screen to screenshot are hardcoded for this script. 

### pdf_merge.py
This script gets every screenshot from the images folder and merge these .png files in the correct order to create a single pdf file. The dimensions for each page of the pdf can be set to any custom value and is hardcoded for this script.

### pdf_maker.py
This script runs pdf_screenshot.py and then pdf_merge.py. The same rules when running pdf_screenshot.py apply here as well.





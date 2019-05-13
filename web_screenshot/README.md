# Web_Screenshot
Web_Screenshot is the web version of ScreenshotScraper, which uses browser automation to generate the pdf. It uses Selenium for the web automation. 

## Setup
One external libraries is used for these scripts - Selenium. <br/>
To install Selenium for Python, check the following link: https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium <br/>
A WebDriver is also needed such as geckodriver for FireFox or edgedriver for Edge (edgedriver is included in this directory).

## Usage
These scripts are best run using the command line.

### single.py 
This script can be used to iterate over multiple pages via URL manipulation and gather screenshots for the different pages. The images will saved to the same directory as PNGs. These PNGs can then be merged using pdf_merge.py and pdf_maker.py in os_screenshot.

### run.py 
This script is an example of a script that can be used to iterate over multiple pages with multiple variables being iterated over in the URL.